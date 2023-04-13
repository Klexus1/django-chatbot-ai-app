from django.conf import settings
from django.shortcuts import render, redirect
import openai

# importing render and redirect
# importing the openai API
# import the generated API key from the secret_key file

API_KEY = getattr(settings, "OPEN_AI_API_KEY")
openai.api_key = API_KEY

# this is the home view for handling home page logic
def chat(request):
    print("Hitting the chat function")
    # the try statement is for sending request to the API and getting back the response
    # formatting it and rendering it in the template
    try:
        # checking if the request method is POST
        if request.method == 'POST':
            # getting prompt data from the form
            prompt = request.POST.get('prompt')
            print("The propt is " + prompt)
            # making a request to the API
            try:
                response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            except Exception as e:
                print(f"Ex {str(e)} occurred.")
                raise
            # formatting the response input
            formatted_response = response['choices'][0]['text']
            # bundling everything in the context
            context = {
                'formatted_response': formatted_response,
                'prompt': prompt
            }
            # this will render the results in the home.html template
            return render(request, 'chat/chat.html', context)
        # this runs if the request method is GET
        else:
            # this will render when there is no request POST or after every POST request
            return render(request, 'chat/chat.html')
    # the except statement will capture any error
    except Exception as e:
        print(f"Er {str(e)} occurred.")
        # this will redirect to the 404 page after any error is caught
        return redirect('error_handler')

# this is the view for handling errors
def error_handler(request):
    return render(request, 'chat/404.html')
