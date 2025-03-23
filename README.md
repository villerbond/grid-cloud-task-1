# grid-and-cloud-task-1

### **Запуск приложения**

1. Собрать и запустить контейнеры с помощью **docker-compose**:
   ```bash
   docker-compose up --build
   ```

2. Docker автоматически создаст два контейнера:
   - **`db`** для PostgreSQL.
   - **`app`** для Flask-приложения.

3. Проверить можно, отправив HTTP-запросы с помощью **curl** или **Postman**.

---

### **Проверка работы**

Чтобы убедиться, что все работает, можно выполнить несколько запросов:

1. **Добавить пользователя** (POST запрос):
   ```bash
   curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d '{"name": "Alice"}'
   ```

2. **Получить список пользователей** (GET запрос):
   ```bash
   curl -X GET http://localhost:8000/users
   ```