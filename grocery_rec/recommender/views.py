from django.shortcuts import render
from django.http import JsonResponse
from .recommender_engine import train_model, get_recommendations

# Create your views here.
def train_view(request):
    try:
        train_model()
        return JsonResponse({"status": "Model trained successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)})
    
def recommend_view(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        return JsonResponse({'error': 'Please provide user_id as a query parameter'}, status=400)
    try:
        user_id = int(user_id)
        recommendations = get_recommendations(user_id)
        return JsonResponse({'user_id': user_id, 'recommendations': recommendations})
    except Exception as e:
        return JsonResponse({'error': str(e)})