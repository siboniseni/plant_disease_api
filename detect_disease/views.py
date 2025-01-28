from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

@csrf_exempt
def disease_detection_view(request):
    if request.method == "POST":
        # Check if the file is in the request
        if 'image' not in request.FILES:
            return JsonResponse({"error": "No image file provided."}, status=400)

        # Get the uploaded file
        image = request.FILES['image']

        # Validate the file type
        if not image.content_type.startswith("image/"):
            return JsonResponse({"error": "Uploaded file is not an image."}, status=400)

        # Save the file temporarily (for now, just to validate it works)
        file_path = default_storage.save(os.path.join('temp', image.name), ContentFile(image.read()))

        # Delete the file after processing (if no longer needed)
        default_storage.delete(file_path)

        return JsonResponse({"message": "Image uploaded successfully!", "filename": image.name})

    return JsonResponse({"error": "Invalid request method."}, status=405)
