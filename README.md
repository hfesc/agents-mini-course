# AI AGENTS MINI CURSO


```bash
mv .env.template .env
# Edit the .env file to add your OpenAI API key

# Build and start the Docker container
make docker-build
make docker-start

# Access Jupyter Notebook
jupyter notebook --port 8080 --allow-root --ip 0.0.0.0 --no-browser
```