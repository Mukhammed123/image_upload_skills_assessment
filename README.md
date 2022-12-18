# Prerequisites:
1. `Python 3.7+`
2. `Node.js` (for frontend)
3. `Python virtualenv` (optional)

# Start Django Server (it has to start at localhost:8000):
1. `cd {project folder}`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

# Start Vue Server
1. `cd {frontend}`
2. `npm install`
3. `npm run dev`


# Requests from Frontend
* Upload Image
```
const data = {
          description: content.value,
          filename: uploadedImgURL.value.file.name,
          location: location.value,
          people: taggedPeople.value,
        }
const formData = new FormData();
        formData.append(
          "file",
          uploadedImgURL.value.file
        );
        formData.append(
          "details",
          JSON.stringify(data)
        );
        
axios.post("http://localhost:8000/api/images/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              "Authorization": store.accessToken
            },
          });
 ```
 
 # Описание
 
 * Перед использованием системы, пользователям необходимо зарегистрироваться
 * При загрузке фотографии можно указывать различную метадату: гео локацию, описание, имена людей на фото
 * Программа может отправлять список фотографий, без мета данных
 * Программа может отправлять фотографию по айди с метаданными
 * Программа может фильтровать фотографии по дате, геолокации, имени человека
 * В системе есть автодополнение по поиску возможных имен людей присутствующих на фотографиях
 
 
