#!/usr/bin/env python3
"""
Create a deployment package for Smithery
"""

import zipfile
import os
from pathlib import Path

def create_deployment_package():
    """Create a ZIP file with only the necessary files for deployment."""
    
    # Files to include in deployment
    include_files = [
        'server.py',
        'requirements.txt',
        'tools/__init__.py',
        'tools/optimize.py',
        'smithery.json',
        'README.md'
    ]
    
    # Create deployment directory
    deploy_dir = Path('deployment')
    deploy_dir.mkdir(exist_ok=True)
    
    # Copy files to deployment directory
    for file_path in include_files:
        src = Path(file_path)
        dst = deploy_dir / file_path
        
        if src.exists():
            # Create parent directories if needed
            dst.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            with open(src, 'r', encoding='utf-8') as f_src:
                with open(dst, 'w', encoding='utf-8') as f_dst:
                    f_dst.write(f_src.read())
            print(f"✅ Copied {file_path}")
        else:
            print(f"⚠️  Warning: {file_path} not found")
    
    # Create ZIP file
    zip_path = Path('prompt-optimizer-mcp-deployment.zip')
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(deploy_dir):
            for file in files:
                file_path = Path(root) / file
                arc_name = file_path.relative_to(deploy_dir)
                zipf.write(file_path, arc_name)
                print(f"📦 Added to ZIP: {arc_name}")
    
    print(f"\n🎉 Deployment package created: {zip_path}")
    print(f"📁 Package size: {zip_path.stat().st_size / 1024:.1f} KB")
    
    # Clean up deployment directory
    import shutil
    shutil.rmtree(deploy_dir)
    print("🧹 Cleaned up temporary files")
    
    return zip_path

if __name__ == "__main__":
    print("🚀 Creating Smithery deployment package...")
    print("=" * 50)
    
    zip_file = create_deployment_package()
    
    print("\n📋 Next steps:")
    print("1. Go to https://smithery.ai/dashboard")
    print("2. Click 'Deploy Server'")
    print("3. Upload the ZIP file:", zip_file.name)
    print("4. Set runtime to: Python 3.11")
    print("5. Set entry point to: server.py")
    print("6. Add environment variable: PYTHONPATH=.")
    print("7. Deploy!")
    
    print("\n🎯 Your MCP server should then be available on Smithery!") 