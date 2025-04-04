# MCP Client

Een Python webapplicatie voor het interacteren met Large Language Models en het verbinden met Model Context Protocol (MCP) servers.

## Wat is MCP Client?

MCP Client is een applicatie die een browser-gebaseerde interface biedt voor gebruikers om te chatten met verschillende LLMs (zoals Claude, GPT, etc.) en de functionaliteit van deze LLMs uit te breiden door verbinding te maken met MCP servers. MCP (Model Context Protocol) is een open standaard die clients en servers in staat stelt om gestructureerd te communiceren over context, tools, en andere capabilities voor LLMs.

Deze applicatie maakt het mogelijk om:
- Met verschillende LLMs te chatten in een gebruiksvriendelijke interface
- MCP servers te configureren en ermee te verbinden
- Tools van MCP servers aan te roepen via LLM chat
- Bestanden en andere resources te delen met LLMs
- Herbruikbare prompts te gebruiken

## Status van het Project

Dit project is in ontwikkeling. Momenteel zijn de volgende onderdelen geïmplementeerd:

- [x] Basisstructuur van het project
- [x] FastAPI backend met MCP API endpoints
- [x] Mock MCP client implementatie
- [x] LLM integratie abstracties
- [x] Configuratiebeheer
- [ ] Chat interface
- [ ] Frontend implementatie
- [ ] Echte MCP SDK integratie
- [ ] Gebruikersauthenticatie

## Installatie

### Vereisten
- Python 3.10 of hoger
- Node.js 16 of hoger (voor frontend ontwikkeling)

### Lokale ontwikkelomgeving
```bash
# Python environment setup
uv venv
source .venv/bin/activate  # Op Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"

# Start de applicatie
python main.py
```

De webinterface is nu beschikbaar op: http://127.0.0.1:8000

### Test API Endpoints

De volgende API endpoints zijn beschikbaar:

- `GET /api/v1/health` - Health check endpoint
- `GET /api/v1/mcp/servers` - Lijst van verbonden MCP servers
- `GET /api/v1/mcp/tools` - Lijst van beschikbare tools
- `GET /api/v1/mcp/resources` - Lijst van beschikbare resources
- `GET /api/v1/mcp/prompts` - Lijst van beschikbare prompts

## Ontwikkeling

Zie [VOLGENDE_STAPPEN.MD](VOLGENDE_STAPPEN.MD) voor meer informatie over de geplande ontwikkeling.

### Project Structuur

```
mcp-client/
├── mcp_client/              # Python package
│   ├── api/                 # FastAPI endpoints
│   ├── core/                # Core functionality
│   │   ├── mcp/            # MCP client implementation
│   │   └── transport/      # Transport implementations
│   ├── config/              # Configuration handling
│   ├── llm/                 # LLM integration
│   ├── static/              # Static web files
│   └── utils/               # Utility functions
├── mcp_client_config/       # Configuration files
├── tests/                   # Test suite
├── frontend/                # Frontend code (React/TypeScript)
├── .env                     # Environment variables
├── PLANNING.MD              # Project planning document
├── TAKEN.MD                 # Project tasks list
└── README.md                # This file
```

### Configuratie

De applicatie gebruikt environment variabelen die kunnen worden ingesteld in het `.env` bestand. Zie `.env.example` voor een voorbeeld.

### MCP Servers Configureren

MCP servers kunnen worden geconfigureerd in het `mcp_client_config/servers.json` bestand:

```json
{
  "servers": [
    {
      "name": "Example MCP Server",
      "url": "http://localhost:3000",
      "transport_type": "sse",
      "auth_token": null,
      "enabled": true,
      "metadata": {
        "description": "Example MCP server for demonstration"
      }
    }
  ]
}
```

## Licentie

Dit project is gelicenseerd onder de MIT-licentie.

## Gerelateerde Projecten

- [MCP Specification](https://spec.modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)