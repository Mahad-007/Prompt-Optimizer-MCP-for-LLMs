# 🚀 Deployment Guide for Prompt Optimizer MCP

This guide will help you deploy your Prompt Optimizer MCP server to Smithery.ai via GitHub.

## ✅ Pre-Deployment Checklist

Before deploying, ensure you have:

1. **All files are committed to GitHub**:
   - ✅ `server.py` - Main MCP server (STDIO mode)
   - ✅ `http_server.py` - HTTP server wrapper
   - ✅ `start.py` - Startup script for both modes
   - ✅ `tools/optimize.py` - Core optimization logic
   - ✅ `requirements.txt` - Python dependencies
   - ✅ `Dockerfile` - Container configuration
   - ✅ `smithery.yaml` - Smithery deployment config
   - ✅ `__init__.py` - Package initialization

2. **Local testing passed**:
   ```bash
   python test_deployment.py
   ```
   Should show: `🎉 All tests passed! Ready for deployment.`

## 🚀 Deployment Steps

### Step 1: Push to GitHub

If you haven't already, push your latest changes:

```bash
git add .
git commit -m "Fix deployment issues and add HTTP server support"
git push origin main
```

### Step 2: Deploy via Smithery.ai

1. **Go to Smithery.ai**: Visit [https://smithery.ai/new](https://smithery.ai/new)

2. **Configure Deployment**:
   - **ID**: `@Mahad-007/prompt-optimizer-mcp-for-llms` (auto-filled from GitHub)
   - **Base Directory**: `.` (root directory)
   - **Local Only**: Leave unchecked

3. **Click "Create"**: This will:
   - Connect to your GitHub repository
   - Build the Docker container
   - Deploy your MCP server
   - Make it publicly available

### Step 3: Monitor Deployment

1. **Check Deployment Status**: Go to the "Deployments" tab
2. **View Logs**: If there are issues, check the build logs
3. **Verify Health**: The server should show "healthy" status

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Build Failures
**Error**: "Unexpected internal error or timeout"
**Solution**: 
- Ensure all dependencies are in `requirements.txt`
- Check that `Dockerfile` is properly configured
- Verify Python version compatibility

#### 2. Import Errors
**Error**: "No module named 'fastmcp'"
**Solution**: 
- Update `requirements.txt` to use `fastmcp>=0.1.0`
- Ensure all imports use correct package names

#### 3. Health Check Failures
**Error**: Health check endpoint not responding
**Solution**:
- Verify `http_server.py` has proper health check endpoint
- Check that port 8000 is exposed in Dockerfile
- Ensure `start.py` correctly handles HTTP mode

#### 4. Server Not Starting
**Error**: Server fails to start
**Solution**:
- Check that `DEPLOYMENT_MODE=http` is set
- Verify `start.py` logic for mode selection
- Ensure proper error handling in server code

### Debugging Steps

1. **Check Local Build**:
   ```bash
   docker build -t prompt-optimizer .
   docker run -p 8000:8000 prompt-optimizer
   ```

2. **Test HTTP Server Locally**:
   ```bash
   set DEPLOYMENT_MODE=http
   python start.py
   ```

3. **Verify Dependencies**:
   ```bash
   pip install -r requirements.txt
   python -c "import fastmcp, fastapi, uvicorn, pydantic; print('All imports successful')"
   ```

## 📊 Deployment Verification

After successful deployment:

1. **Check Server URL**: Your server will be available at:
   ```
   https://smithery.ai/server/@Mahad-007/prompt-optimizer-mcp-for-llms
   ```

2. **Test Endpoints**:
   ```bash
   # Health check
   curl https://your-server-url/
   
   # Optimize prompt
   curl -X POST https://your-server-url/optimize \
     -H "Content-Type: application/json" \
     -d '{"raw_prompt": "Write about AI", "style": "creative"}'
   
   # Score prompt
   curl -X POST https://your-server-url/score \
     -H "Content-Type: application/json" \
     -d '{"raw_prompt": "Write about AI", "improved_prompt": "Explain artificial intelligence"}'
   ```

3. **Update MCP Client Configuration**:
   ```json
   {
     "mcpServers": {
       "prompt-optimizer": {
         "command": "npx",
         "args": ["-y", "@smithery/cli", "connect", "@Mahad-007/prompt-optimizer-mcp-for-llms"]
       }
     }
   }
   ```

## 🔄 Continuous Deployment

Once deployed, any changes pushed to your GitHub repository will automatically trigger a new deployment.

### Update Process:
1. Make changes to your code
2. Test locally: `python test_deployment.py`
3. Commit and push: `git push origin main`
4. Smithery.ai will automatically redeploy

## 📞 Support

If you encounter issues:

1. **Check Smithery.ai Documentation**: [https://smithery.ai/docs](https://smithery.ai/docs)
2. **Review Build Logs**: Look for specific error messages
3. **Test Locally**: Ensure everything works before deploying
4. **Check Dependencies**: Verify all packages are available

---

**🎉 Congratulations!** Your Prompt Optimizer MCP server should now be successfully deployed and accessible via Smithery.ai. 