@echo off
echo ====================================
echo 推送到 GitHub 仓库
echo ====================================
echo.
echo 正在推送到: https://github.com/pengyuanzhi/RebelliousNature.git
echo.
cd /d "%~dp0"
echo.
echo 如果推送失败，请先登录 GitHub：
echo 1. 运行命令: gh auth login
echo 2. 或访问: https://github.com/login
echo.
pause
git push -u origin master
echo.
echo ====================================
echo 推送完成！
echo ====================================
pause
