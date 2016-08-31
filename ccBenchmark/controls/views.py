from .models import Control
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import ControlForm, RemediationForm
from django.shortcuts import redirect


def control_list(request):
    # controls = Control.objects.filter(title__contains='backup')
    controls = Control.objects.all()
    return render(request, 'controls/control_list.html', {'controls':  controls})


def control_detail(request, pk):
    control = get_object_or_404(Control, pk=pk)
    return render(request, 'controls/control_detail.html', {'control': control})


def control_new(request):
    if request.method == "POST":
        form = ControlForm(request.POST)
        if form.is_valid():
            control = form.save(commit=False)
            control.save()
            return redirect('control_detail', pk=control.pk)
    else:
        form = ControlForm()

    return render(request, 'controls/control_edit.html', {'form': form})


def control_edit(request, pk):
    control = get_object_or_404(Control, pk=pk)
    if request.method == "POST":
        form = ControlForm(request.POST, instance=control)
        if form.is_valid():
            control = form.save(commit=False)
            control.save()
            return redirect('control_detail', pk=control.pk)
    else:
        form = ControlForm(instance=control)

    return render(request, 'controls/control_edit.html', {'form': form})


def remediation_new(request):
    if request.method == "POST":
        form = RemediationForm(request.POST)
        if form.is_valid():
            remediation = form.save(commit=False)
            remediation.who = request.user
            remediation.remediation_date = timezone.now()
            remediation.save()
            return redirect('control_list')
    else:
        form = RemediationForm()

    return render(request, 'controls/rem_edit.html', {'form': form})


def remediation_edit(request, pk):
    remediation = get_object_or_404(Control, pk=pk)
    if request.method == "POST":
        form = ControlForm(request.POST, instance=remediation)
        if form.is_valid():
            remediation = form.save(commit=False)
            remediation.save()
            return redirect('control_list')
    else:
        form = ControlForm(instance=remediation)

    return render(request, 'controls/rem_edit.html', {'form': form})