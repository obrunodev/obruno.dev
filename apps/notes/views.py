from apps.notes.forms import NoteForm
from apps.notes.models import Note
from core.utils.pagination import paginate

from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render


def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser)
def notes_create(request):
    if request.method == 'GET':
        form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('notes:list')

    context = {'form': form}
    return render(request, 'notes/notes_form.html', context)


@login_required
@user_passes_test(is_superuser)
def notes_list(request):
    query = request.GET.get('q', '')
    notes = Note.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query),
        user=request.user,
    )
    page_obj = paginate(request, notes)
    context = {'notes': page_obj}
    return render(request, 'notes/notes_list.html', context)


@login_required
@user_passes_test(is_superuser)
def notes_update(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'GET':
        form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:list')

    context = {'form': form}
    return render(request, 'notes/notes_form.html', context)


@login_required
@user_passes_test(is_superuser)
def notes_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')

    context = {'note': note}
    return render(request, 'notes/notes_confirm_delete.html', context)


@login_required
@user_passes_test(is_superuser)
def notes_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    context = {'note': note}
    return render(request, 'notes/notes_detail.html', context)
