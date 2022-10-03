# itFox

SERVER IP: 3.73.56.209
Deployed with gunicorn & nginx & AWS

Available routes:

    • ADMIN PANEL - /admin
    superuser login: django
    superuser password: django
    
    • POST auth /api/v1/auth/
    
    • GET news /api/v1/news/
    • POST news /api/v1/news/
    • PUT news /api/v1/news/<news_id>
    • DELETE news /api/v1/news/<news_id>
    
    • GET comments /api/v1/news/<news_id>/comments
    • POST comments /api/v1/news/<news_id>/comments
    • DELETE comments /api/v1/news/<news_id>/comments/<comments_id>
    • PUT comments /api/v1/news/<news_id>/comments/<comments_id>
    
    • POST like /api/v1/news/<news_id>/like/
    • POST unlike /api/v1/news/<news_id>/unlike/


Made by Nikolay "FourZd" Ryaskov
