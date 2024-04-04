# Medicinal Plant Identification And Retrieval-Augmented Generation (RAG) Chatbot

This project, developed for the Smart India Hackathon (SIH) 2023, encompasses the fusion of two critical functionalities: Medicinal Plant Identification and Retrieval-Augmented Generation (RAG) Chatbot. The aim is to provide a comprehensive solution for identifying medicinal plants and generating informative content about them, leveraging advanced machine learning and natural language processing techniques.

## Overview

The Medicinal Plant Identification And Retrieval-Augmented Generation (RAG) Chatbot is a multifaceted project designed to address the growing need for accessible information on medicinal plants. It combines image recognition for plant identification with advanced text generation capabilities to provide users with detailed and accurate insights into various medicinal plants.

## Functionalities

### Medicinal Plant Identification

The project incorporates a robust Medicinal Plant Identification system. Key features include:

- Utilization of a medicinal plant dataset sourced from Kaggle.
- Retraining of the InceptionV3 model on the dataset, employing machine learning practices such as data augmentation to enhance accuracy and performance.
- Seamless integration of the identification functionality into the chatbot interface, enabling users to upload images of plants for identification.

### Retrieval-Augmented Generation (RAG) Chatbot

The RAG Chatbot component of the project leverages advanced natural language processing techniques to provide users with informative content. Key features include:

- Implementation of InstructEmbeddings for embedding generation.
- Integration of the OpenAI GPT-3.5-Turbo model for text generation.
- Generation of contextually relevant and informative responses based on user queries, ensuring a rich and engaging user experience.

### Backend Architecture

The backend architecture of the project is built using the Django Rest Framework, providing seamless compatibility across multiple platforms. Key features include:

- Utilization of Django's robust and scalable framework for developing RESTful APIs.
- Implementation of secure and efficient data handling mechanisms.
- Provision of seamless communication between the frontend interface and the machine learning models powering the identification and generation functionalities.

## Team Contribution

As part of the development team for this project, the responsibilities undertaken include:

- Designing and implementing the backend architecture to support the project's functionalities.
- Developing the Retrieval-Augmented Generation (RAG) Chatbot functionality, integrating InstructEmbeddings and OpenAI GPT-3.5-Turbo model.
- Leading the development efforts for the Medicinal Plant Identification functionality, including dataset selection, model training, and integration into the overall system.

## Future Enhancements

While the current version of the Medicinal Plant Identification And Retrieval-Augmented Generation (RAG) Chatbot provides a robust foundation, several enhancements can be explored in the future, including:

- Integration of additional machine learning models for improved plant identification accuracy.
- Expansion of the medicinal plant dataset to include a wider variety of species.
- Incorporation of user feedback mechanisms to continuously improve the chatbot's responses and functionalities.


## Usage

To utilize the Medicinal Plant Identification And Retrieval-Augmented Generation (RAG) Chatbot, follow these steps:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/PhaleshM/SIH_backend.git
   ```

2. Navigate to the project directory

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

5. Install dependencies from requirements.txt:

   ```
   pip install -r requirements.txt
   ```

6. Start the Django development server:

   ```
   python manage.py runserver
   ```

7. Access Medicinal Plant Identification functionality:
   
   - Navigate to `localhost:8000/api/predict/` in your web browser.
   - Upload an image of the medicinal plant for identification.

8. Access Retrieval-Augmented Generation (RAG) functionality:
   
   - Create embeddings for your own data using InstructEmbeddings.
   - Integrate the embeddings into the chatbot for text generation.

Note: The embeddings generated for Retrieval-Augmented Generation can be large in size, making it impractical to share. Therefore, you need to generate embeddings based on your specific data. Follow the instructions provided by InstructEmbeddings for creating embeddings.

