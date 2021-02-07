
color 0e
@echo off
   :menu
   cls
   echo.  =================================================
   echo.
   echo.  DJANGO SYSTEM MANAGEMENT - manage.py
   echo.
   echo   -------------------------------------------------
   echo       (A)bout
   echo.
   echo   SETTINGS
   echo       (P)RINT_settings PRINT SETTINGS.py
   echo       (F)IND string in print_settings   
   echo. 
   echo   MODEL 
   echo       (M)ODELS list - list_model_info --force-color
   echo       (D)umpdata DUMPDATA
   echo       MA(K)Emigrations - gen query scripts
   echo       MI(G)RATE - send queries to db server (L)--fake
   echo.
   echo   URL
   echo       (U)RLs - show_urls
   echo.        
   echo       E(X)it (N)otepad (S)hell 
   echo.
   echo     Comment here   put notes here for bettering menu
   echo.  =================================================
   echo.
   choice /c:AGKDPMUSXFNL > nul
   if errorlevel 12 goto L  
   if errorlevel 11 goto N  
   if errorlevel 10 goto F  
   if errorlevel 9 goto end   
   if errorlevel 8 goto S   
   if errorlevel 7 goto U   
   if errorlevel 6 goto M   
   if errorlevel 5 goto P   
   if errorlevel 4 goto D
   if errorlevel 3 goto K
   if errorlevel 2 goto G
   if errorlevel 1 goto A
   echo Error... choice not installed
   goto end
   :N
   notepad h.bat
   goto menu
   :A
   echo press Q,W,D,P,M,U or S to run a manage.py subcommand
   pause
   goto menu
   :G
   python manage.py migrate
   pause
   goto menu
   :L
   python manage.py migrate --fake
   pause
   goto menu
   :K  
   python manage.py makemigrations
   pause
   goto menu
   :D
   echo python manage.py dumpdata
   python manage.py dumpdata
   pause
   goto menu
   :P
   python manage.py print_settings
   pause
   goto menu
   :F
   set /p UserString=Enter a few characters to find?   
   python manage.py print_settings | find "%UserString%" /I
   pause
   goto menu   
   :M
   python manage.py list_model_info --force-color
   pause
   goto menu
   :U
   python manage.py show_urls
   pause
   goto menu
   :S
   python manage.py shell
   pause
   goto menu
   :end 
