# Overview

TechDay is a web-based feedback dashboard application built with Flask that allows users to submit and view feedback data related to presentations and projects. The application provides a modern, gradient-styled interface for collecting structured feedback through JSON API endpoints and displaying it in a dashboard format.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Uses Flask's built-in Jinja2 templating system to serve HTML pages
- **Styling**: Custom CSS with modern design patterns including gradients, backdrop filters, and responsive grid layouts
- **Layout**: Grid-based dashboard design with two-column layout for displaying feedback data
- **UI Framework**: Pure CSS implementation without external frameworks, focusing on modern glassmorphism design

## Backend Architecture
- **Web Framework**: Flask (Python) serving as a lightweight web server
- **Route Structure**: RESTful API design with separate endpoints for serving pages and handling data
- **Data Storage**: In-memory storage using Python lists (temporary storage solution)
- **Error Handling**: Comprehensive try-catch blocks with proper HTTP status codes and JSON error responses
- **Logging**: Built-in Python logging for debugging and monitoring

## API Design
- **POST /recibir-feedback**: Accepts JSON payloads with presentation and project summaries
- **GET /**: Serves the main dashboard interface
- **GET /get-feedback**: Endpoint for retrieving stored feedback (implementation incomplete)
- **Data Validation**: Server-side validation for required JSON fields before processing

## Security Considerations
- **Session Management**: Flask secret key configuration with environment variable fallback
- **Input Validation**: JSON payload validation for required fields
- **Error Sanitization**: Generic error messages to prevent information leakage

# External Dependencies

## Core Dependencies
- **Flask**: Primary web framework for routing, templating, and HTTP handling
- **Python Standard Library**: Uses `os` for environment variables and `logging` for application monitoring

## Runtime Environment
- **Environment Variables**: Configurable session secret through `SESSION_SECRET` environment variable
- **Template Directory**: Standard Flask templates directory structure for HTML files

## Potential Integration Points
- The current in-memory storage suggests the application is designed for development/testing and would benefit from persistent database integration
- The feedback collection system appears designed for real-time data aggregation, indicating potential for database or external API integration
- The incomplete `/get-feedback` endpoint suggests planned functionality for data retrieval and possibly external system integration