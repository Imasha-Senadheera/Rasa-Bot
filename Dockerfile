# Stage 1: Build stage
FROM python:3.8-slim AS builder

# Install Rasa and its dependencies
RUN python -m pip install rasa

# Set working directory inside the container
WORKDIR /app

# Copy the project files
COPY . .

# Train the NLU model
RUN rasa train nlu

# Stage 2: Final stage
FROM python:3.8-alpine AS final

# Set working directory inside the container
WORKDIR /app

# Copy only the trained NLU model from the builder stage
COPY --from=builder /app/models/nlu.tar.gz /app/models/nlu.tar.gz

# Expose the Rasa API port
EXPOSE 8080

# Set the user to run, don't run as root
USER 1000

# Set the entrypoint for interactive shells
ENTRYPOINT ["rasa"]

# Command to launch Rasa chatbot
CMD ["run", "--enable-api", "--port", "8080"]
