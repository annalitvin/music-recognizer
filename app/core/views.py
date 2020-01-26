from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from core.utils import get_lyrics, get_audio_file

# Create your views here.

@csrf_exempt
def index(request):

    rec_result = None

    if request.POST.get('action') == 'get_file_body':

        song_base64 = request.POST.get('data')
        rec_result = get_audio_file(song_base64.strip()).get('result')

        if rec_result is not None:
            song_deezer = rec_result.get("deezer")
            if song_deezer:
                deezer_id = song_deezer.get("id")
                return JsonResponse({'deezer_id': deezer_id})

    if request.POST.get('action') == 'post':

        lyrics = request.POST.get('input_text')
        audio_data = request.POST.get('data')
        rec_result = get_lyrics(lyrics)

        return JsonResponse({'song_id': rec_result})

    return render(request, 'base.html')
