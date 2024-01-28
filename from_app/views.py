from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from from_app.form import Forms
from from_app.models import Form


# Create your views here.
def IndexPage(request):
    form = Form.objects.all()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def post(request):
    forms = Forms(request.POST)
    if forms.is_valid():
        forms.save()
        return redirect('home')
    else:
        return render(request, 'form.html')


def show(request, id):
    model = Form.objects.get(id=id)
    context = {
        'info': model
    }
    return render(request, 'show.html', context)


def update_view(request, pk):
    instance = get_object_or_404(Form, pk=pk)
    form = Forms(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect(
            'home')  # Replace 'success_url' with the actual URL you want to redirect to upon successful update
    return render(request, 'form.html', context={
        'i': instance
    })


def delete_view(request, pk):
    instance = get_object_or_404(Form, pk=pk)

    if request.method == 'POST':
        instance.delete()
        return redirect('home')  # Replace 'home' with the actual URL you want to redirect to upon successful deletion

    return render(request, 'form.html', {'instance': instance})
