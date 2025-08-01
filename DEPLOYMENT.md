# 🚀 Smithery Deployment Guide

This guide will walk you through deploying your Prompt Optimizer MCP server to Smithery.

## 📋 Prerequisites

1. **Smithery Account**: Sign up at [smithery.ai](https://smithery.ai)
2. **Smithery CLI**: Install the command-line interface
3. **Docker**: Ensure Docker is installed and running
4. **Git**: For version control (optional but recommended)

## 🛠️ Installation Steps

### 1. Install Smithery CLI

**Using npm:**
```bash
npm install -g @smithery/cli
```

**Using yarn:**
```bash
yarn global add @smithery/cli
```

**Verify installation:**
```bash
smithery --version
```

### 2. Authenticate with Smithery

```bash
smithery auth login
```

Follow the prompts to log in to your Smithery account.

## 🚀 Deployment Options

### Option 1: Automated Deployment (Recommended)

**For Linux/macOS:**
```bash
chmod +x deploy.sh
./deploy.sh
```

**For Windows:**
```cmd
deploy.bat
```

### Option 2: Manual Deployment

1. **Validate your project:**
   ```bash
   smithery validate
   ```

2. **Deploy to Smithery:**
   ```bash
   smithery deploy
   ```

3. **Check deployment status:**
   ```bash
   smithery status
   ```

## 📁 Project Structure for Deployment

Your project should have this structure:
```
prompt-optimizer-mcp/
├── smithery.yaml          # Smithery configuration
├── Dockerfile             # Container configuration
├── .dockerignore          # Docker ignore file
├── requirements.txt       # Python dependencies
├── server.py              # Main MCP server
├── tools/
│   ├── __init__.py
│   └── optimize.py        # Core optimization logic
├── deploy.sh              # Linux/macOS deployment script
└── deploy.bat             # Windows deployment script
```

## ⚙️ Configuration Details

### smithery.yaml
- **Runtime**: Python 3.11
- **Resources**: 0.5 CPU, 512MB RAM
- **Scaling**: 1-5 replicas
- **Health Check**: `/health` endpoint
- **Domain**: `prompt-optimizer-mcp.smithery.ai`

### Dockerfile
- **Base Image**: Python 3.11-slim
- **Security**: Non-root user
- **Health Check**: Python process monitoring
- **Port**: 8000 (for health checks)

## 🔍 Post-Deployment

### Check Deployment Status
```bash
smithery status
```

### View Logs
```bash
smithery logs
```

### Monitor Performance
```bash
smithery metrics
```

### Update Deployment
```bash
smithery deploy --force
```

## 🌐 Accessing Your MCP Server

Once deployed, your MCP server will be available at:
- **URL**: `https://prompt-optimizer-mcp.smithery.ai`
- **Health Check**: `https://prompt-optimizer-mcp.smithery.ai/health`

## 🔧 Troubleshooting

### Common Issues

1. **"Smithery CLI not found"**
   - Reinstall: `npm install -g @smithery/cli`
   - Check PATH: `echo $PATH`

2. **"Authentication failed"**
   - Re-login: `smithery auth login`
   - Check token: `smithery auth status`

3. **"Build failed"**
   - Check Docker: `docker --version`
   - Validate config: `smithery validate`

4. **"Deployment timeout"**
   - Check resources in `smithery.yaml`
   - Increase timeout settings

### Debug Commands

```bash
# Validate configuration
smithery validate

# Check build logs
smithery logs --build

# Force rebuild
smithery deploy --force --rebuild

# Check resource usage
smithery metrics --cpu --memory
```

## 📊 Monitoring and Maintenance

### Health Monitoring
- **Automatic**: Smithery monitors your service
- **Manual**: Check `/health` endpoint
- **Alerts**: Configure in Smithery dashboard

### Scaling
- **Auto-scaling**: Based on CPU usage (70%)
- **Manual scaling**: `smithery scale --replicas 3`

### Updates
- **Code changes**: `smithery deploy --force`
- **Configuration**: Update `smithery.yaml` and redeploy
- **Dependencies**: Update `requirements.txt` and redeploy

## 🔐 Security Considerations

- ✅ Non-root user in container
- ✅ Minimal base image (slim)
- ✅ No sensitive data in code
- ✅ Health checks enabled
- ✅ Resource limits configured

## 💰 Cost Optimization

- **Resources**: Start with minimal (0.5 CPU, 512MB RAM)
- **Scaling**: Use auto-scaling to handle traffic
- **Monitoring**: Watch usage in Smithery dashboard

## 📞 Support

- **Smithery Docs**: [docs.smithery.ai](https://docs.smithery.ai)
- **Community**: [discord.gg/smithery](https://discord.gg/smithery)
- **Issues**: Create issue in this repository

## ✅ Deployment Checklist

- [ ] Smithery CLI installed
- [ ] Authenticated with Smithery
- [ ] All files present (smithery.yaml, Dockerfile, etc.)
- [ ] Tests passing locally
- [ ] Configuration validated
- [ ] Deployment successful
- [ ] Health check passing
- [ ] Domain accessible
- [ ] Logs clean
- [ ] Performance acceptable 