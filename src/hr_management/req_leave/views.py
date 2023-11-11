from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404, HttpResponse
# Messages used for cancelling request unavailability
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST
# Necessary for making queries; Retrieving corresponding employee(s)
from django.db import models
from .models import *
# For adding absences to Calendar
from calendar_app.models import Absence_Calendar
from .forms import *


# View all requests
def view_request(request):

    # Utilize this alongside a function to obtain the current
    # logged in employee's ID (MAKE SURE TO GET CORRECT EMPLOYEE_ID)
    # get_logged_employee = ... (Use Django's method)
    # get_logged_employee = "Cowman"
    # request_query = Request.objects.filter(employee_id=get_logged_employee)

    # Comment / Remove this
    view_request = Request.objects.all()

    # Change view_request to request_query
    # Calculating days requested per request
    for leave_request in view_request:
        leave_request.days_requested = \
            days_requested(leave_request.start_date, leave_request.end_date)

    # Comment / Remove this
    context = {"view_request": view_request}

    # Uncomment this
    # context = {"view_request": request_query}
    return render(request, "view_request.html", context)


# Creates a leave request form
def submit_request(request):

    request_form = RequestCreateForm(request.POST or None)

    if request_form.is_valid():
        
        request_form.save()
        request_form = RequestCreateForm()

        return redirect(reverse("req_leave:submit_request"))


    context = {"request_form": request_form}
    return render(request, "request.html", context)


# Canceling submitted request, for the employee
# in case of accidental / erroneous request
def cancel_request(request, id):

    cancel_request = get_object_or_404(Request, id=id)

    if cancel_request.request_status != "Pending":
        messages.info(request, "Can't cancel request that has been attended!")
        return redirect("../../view")

    if request.method == "POST":
        
        cancel_request.delete()
        return redirect("../../view")

    context = {"request": cancel_request}
    return render(request, "view_request.html", context)


# For managing requests
def manage_request(request):

    if request.method == 'POST':

        form = RequestCreateForm(request.POST)

        if form.is_valid():

            action = form.cleaned_data.get('manage_request')
            pk = form.cleaned_data.get('request_id')
            leave_request = get_object_or_404(Request, pk=pk)

            if action == 'Accept':
                leave_request.request_status = 'Accepted'

            elif action == 'Decline':
                leave_request.request_status = 'Declined'

            leave_request.save()
    else:
        form = RequestCreateForm()

    view_request = Request.objects.all()
    
    for leave_request in view_request:
        leave_request.days_requested = \
            days_requested(leave_request.start_date, leave_request.end_date)

    context = {"view_request": view_request, "form": form}
    return render(request, "manage_request.html", context)



# Utilized for updating the request status
# that is when a form is updated (POST)
@require_POST
def update_request_status(request, pk):
    leave_request = get_object_or_404(Request, pk=pk)
    action = request.POST.get('action')

    if action == 'accept':

        # Check if it has already been Accepted
        # Dont do anything
        if leave_request.request_status == 'Accepted':
            return redirect('req_leave:manage_request')

        leave_request.request_status = 'Accepted'

        # Send data to calendar_app's Calendar models.py
        Absence_Calendar.objects.create(
            employee_id = leave_request.employee_id,
            absent_date_start = leave_request.start_date,
            absent_date_end = leave_request.end_date,
        )

        print("I am here")

    elif action == 'decline':

        # Check if it has already been Declined
        # Dont do anything
        if leave_request.request_status == 'Declined':
            return redirect('req_leave:manage_request')

        leave_request.request_status = 'Declined'

    leave_request.save()

    return redirect('req_leave:manage_request')
