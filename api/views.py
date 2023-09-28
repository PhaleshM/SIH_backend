# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .ml_predictor import PlantPredictor
from PIL import Image
from django.http import JsonResponse

# Define your class_names and image_size here
class_names=['Alpinia Galanga (Rasna)', 'Amaranthus Viridis (Arive-Dantu)', 'Artocarpus Heterophyllus (Jackfruit)', 'Azadirachta Indica (Neem)', 'Basella Alba (Basale)', 'Brassica Juncea (Indian Mustard)', 'Carissa Carandas (Karanda)', 'Citrus Limon (Lemon)', 'Ficus Auriculata (Roxburgh fig)', 'Ficus Religiosa (Peepal Tree)', 'Hibiscus Rosa-sinensis', 'Jasminum (Jasmine)', 'Mangifera Indica (Mango)', 'Mentha (Mint)', 'Moringa Oleifera (Drumstick)', 'Muntingia Calabura (Jamaica Cherry-Gasagase)', 'Murraya Koenigii (Curry)', 'Nerium Oleander (Oleander)', 'Nyctanthes Arbor-tristis (Parijata)', 'Ocimum Tenuiflorum (Tulsi)', 'Piper Betle (Betel)', 'Plectranthus Amboinicus (Mexican Mint)', 'Pongamia Pinnata (Indian Beech)', 'Psidium Guajava (Guava)', 'Punica Granatum (Pomegranate)', 'Santalum Album (Sandalwood)', 'Syzygium Cumini (Jamun)', 'Syzygium Jambos (Rose Apple)', 'Tabernaemontana Divaricata (Crape Jasmine)', 'Trigonella Foenum-graecum (Fenugreek)']
image_size = (299, 299)

# Initialize the predictor with the model and dependencies
predictor = PlantPredictor('inceptionv4_medicinal_plant_model3.h5', class_names, image_size)

@api_view(['POST'])
def predict_image_view(request):
    if request.method == 'POST' and request.FILES['image']:
        # Get the uploaded image from the request
        uploaded_image = request.FILES['image']
        
        # Open the uploaded image using Pillow
        try:
            image = Image.open(uploaded_image)
            image = image.resize(image_size)  # Resize if needed
        except Exception as e:
            return JsonResponse({'error': 'Invalid image format.'}, status=400)

        # Use the loaded image with your model for prediction
        prediction = predictor.predict(image)
        
        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

