import os
import math
import warnings
import joblib
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from .models import student

warnings.filterwarnings('ignore')

def home(request):
    student_name = request.session.get('student_name')
    return render(request, 'home.html', {'student_name': student_name})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if name and password:
            if student.objects.filter(name=name).exists():
                return render(request, 'signup.html', {'error': 'User already registered with this name! Please Login.'})
            
            # Save data into DB table
            student.objects.create(name=name, email=email, password=password)
            return render(request, 'login.html', {'msg': 'Registration Successful! Please login below.'})
        else:
            return render(request, 'signup.html', {'error': 'Please fill all required fields.'})
            
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def loginvalidation(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        password = request.POST.get('password', '').strip()

        try:
            user = student.objects.get(name=name, password=password)
            # Validation success -> store user session
            request.session['student_name'] = user.name
            request.session['student_email'] = user.email or ''
            request.session['student_id'] = user.id
            return redirect('input')
        except student.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid User! User does not exist or password is wrong.'})
    
    return redirect('login')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def input(request):
    student_name = request.session.get('student_name', 'Student')
    return render(request, 'input.html', {'student_name': student_name})

def result(request):
    student_name = request.session.get('student_name', 'Student')
    
    # Accept inputs from either POST or GET
    params = request.POST if request.method == 'POST' else request.GET

    try:
        cgpa_raw = params.get('cgpa', '').strip()
        iq_raw = params.get('iq', '').strip()
        profile_raw = params.get('profile_score', '').strip()

        if not cgpa_raw or not iq_raw or not profile_raw:
            return render(request, 'input.html', {
                'error': 'Please provide all three assessment values: CGPA, Aptitude/IQ Score, and Profile Score.',
                'student_name': student_name,
                'cgpa': cgpa_raw,
                'iq': iq_raw,
                'profile_score': profile_raw
            })

        cgpa = float(cgpa_raw)
        iq = float(iq_raw)
        profile_score = float(profile_raw)

        # Realistic academic validation
        if not (0.0 <= cgpa <= 10.0):
            return render(request, 'input.html', {
                'error': 'Academic CGPA must be on a 0.00 to 10.00 scale.',
                'student_name': student_name,
                'cgpa': cgpa, 'iq': iq, 'profile_score': profile_score
            })
        if not (40 <= iq <= 160):
            return render(request, 'input.html', {
                'error': 'Aptitude/IQ score must be within the typical assessment range (40 - 160).',
                'student_name': student_name,
                'cgpa': cgpa, 'iq': iq, 'profile_score': profile_score
            })
        if not (0 <= profile_score <= 100):
            return render(request, 'input.html', {
                'error': 'Profile Score must be between 0 and 100.',
                'student_name': student_name,
                'cgpa': cgpa, 'iq': iq, 'profile_score': profile_score
            })

        scaler_path = os.path.join(settings.BASE_DIR, 'sp_scaler_Model.pkl')
        model_path = os.path.join(settings.BASE_DIR, 'sp_Model.pkl')

        scaler = joblib.load(scaler_path)
        mlmodel = joblib.load(model_path)

        scaled_input = scaler.transform([[cgpa, iq, profile_score]])
        ans = int(mlmodel.predict(scaled_input)[0])

        # Placement Probability using logistic transformation of decision margin
        decision_val = float(mlmodel.decision_function(scaled_input)[0])
        prob = round((1.0 / (1.0 + math.exp(-decision_val))) * 100, 1)

        # Authentic evaluation feedback based on college T&P benchmarks
        if cgpa >= 7.5:
            cgpa_status = "Excellent"
            cgpa_remark = "Meets cutoffs for Tier-1 Product & Consulting Companies"
            cgpa_level = "high"
        elif cgpa >= 6.5:
            cgpa_status = "Good"
            cgpa_remark = "Eligible for Mass IT Recruiters & Standard Drives"
            cgpa_level = "medium"
        else:
            cgpa_status = "Needs Improvement"
            cgpa_remark = "Below the standard 6.5 CGPA initial screening cutoff"
            cgpa_level = "low"

        if iq >= 105:
            iq_status = "Strong"
            iq_remark = "High probability of clearing preliminary aptitude & logical rounds"
            iq_level = "high"
        elif iq >= 90:
            iq_status = "Moderate"
            iq_remark = "Capable, but speed and accuracy drills are recommended"
            iq_level = "medium"
        else:
            iq_status = "Critical Area"
            iq_remark = "Needs regular practice on quantitative and reasoning tests"
            iq_level = "low"

        if profile_score >= 70:
            profile_status = "Outstanding"
            profile_remark = "Impressive technical projects, certifications & extracurricular profile"
            profile_level = "high"
        elif profile_score >= 50:
            profile_status = "Average"
            profile_remark = "Decent base; add 1-2 deployed full-stack or domain-specific projects"
            profile_level = "medium"
        else:
            profile_status = "Developing"
            profile_remark = "Focus on building real-world projects and participating in hackathons"
            profile_level = "low"

        # Actionable Placement Cell recommendations
        tips = []
        if cgpa < 7.0:
            tips.append("Academic Focus: Aim to score >= 7.5 SGPA in upcoming semesters to elevate your aggregate CGPA above the primary company screening threshold.")
        else:
            tips.append("Academic Consistency: Maintain your current GPA trajectory and ensure all academic records/transcripts are up to date.")

        if iq < 100:
            tips.append("Aptitude Preparation: Solve daily 30-minute timed mock tests on Quantitative Aptitude, Logical Reasoning, and Data Interpretation.")
        else:
            tips.append("Aptitude Advantage: High analytical score. Concentrate on company-specific online assessment patterns (TCS NQT, Cognizant, Infosys, Capgemini).")

        if profile_score < 65:
            tips.append("Technical Portfolio: Build at least two functional web/software projects with public GitHub repositories and clean documentation.")
        else:
            tips.append("Interview Readiness: Your technical profile is strong; focus on explaining system architecture and answering core CS fundamental questions (OOP, DBMS, OS, Networks).")

        context = {
            'student_name': student_name,
            'ans': ans,
            'prob': prob,
            'cgpa': f"{cgpa:.2f}",
            'iq': int(iq),
            'profile_score': int(profile_score),
            'cgpa_status': cgpa_status,
            'cgpa_remark': cgpa_remark,
            'cgpa_level': cgpa_level,
            'iq_status': iq_status,
            'iq_remark': iq_remark,
            'iq_level': iq_level,
            'profile_status': profile_status,
            'profile_remark': profile_remark,
            'profile_level': profile_level,
            'tips': tips
        }
        return render(request, 'result.html', context)
    except Exception as e:
        return render(request, 'input.html', {
            'error': f'Prediction could not be completed: {str(e)}',
            'student_name': student_name
        })
