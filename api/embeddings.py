import pickle
import textwrap
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS



def load_embeddings(store_name, path):
    with open(f"{path}/faiss_{store_name}.pkl", "rb") as f:
        VectorStore = pickle.load(f)
    return VectorStore

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

def process_llm_response(llm_response):
    print(wrap_text_preserve_newlines(llm_response['result']))
    print('\nSources:')
    for source in llm_response["source_documents"]:
        print(source.metadata['source'])

def main():
    # Set up the environment

    # Define your embedding store path
    Embedding_store_path = f"/Data"  # Make sure root_dir is defined somewhere

    # Load the embeddings (only needs to be done once)
    db_instructEmbedd = load_embeddings(sotre_name='instructEmbeddings', path=Embedding_store_path)

    # Create the retriever
    retriever = db_instructEmbedd.as_retriever(search_kwargs={"k": 5})

    # Create the chain to answer questions (only needs to be done once)
    qa_chain_instrucEmbed = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0.2),
                                                        chain_type="stuff",
                                                        retriever=retriever,
                                                        return_source_documents=True)

    # Query and process responses
    predicted_species = 'Alpinia Galanga (Rasna)'  # Replace this with your predicted species
    query = f'Give all the information about {predicted_species}'
    
    print(f'-------------------Information about {predicted_species}------------------\n')
    llm_response = qa_chain_instrucEmbed(query)
    process_llm_response(llm_response)

if __name__ == "__main__":
    main()
