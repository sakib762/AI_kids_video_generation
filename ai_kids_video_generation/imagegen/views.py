from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import replicate
import os
import replicate
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the Replicate API token
replicate_token = os.getenv("REPLICATE_API_TOKEN")

# Check if token loaded
if not replicate_token:
    raise ValueError("Replicate API token is not defined. Check your .env file.")

# Set the token for replicate to use
replicate.Client(api_token=replicate_token)
@csrf_exempt
def generate_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt')
            model = replicate.models.get("cjwbw/stable-diffusion-v1-4")
            version = model.versions.get("db21e45f7075e206da8d0fdb1df0bbd43f13f40e52cfd32e34b9c7cd99f26b97")

            output = version.predict(prompt=prompt)
            return JsonResponse({"image_url": output[0]})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)  
    
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)
