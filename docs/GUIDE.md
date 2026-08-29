# Project Guide

## Overview

This project provides a comprehensive solution for managing user data and processing transactions efficiently.

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn
- PostgreSQL 14+

### Installation

```bash
npm install
npm run setup
npm start
```

## Architecture

The application follows a layered architecture:

```
src/
├── api/          # REST API endpoints
├── services/     # Business logic
├── models/       # Data models
├── utils/        # Helper functions
└── config/       # Configuration files
```

## API Reference

See [API Documentation](./API.md) for detailed endpoint information.

## Configuration

Environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |
| DB_HOST | Database host | localhost |
| DB_NAME | Database name | app_db |
| LOG_LEVEL | Logging level | info |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details.
