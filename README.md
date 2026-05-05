# 📝 Blog API

A production-ready RESTful backend API built with **FastAPI** and **PostgreSQL** — supporting user authentication, blog post management, comments, likes, and role-based admin control.

🔗 **Live API:** [https://blog-api-9n0c.onrender.com/docs](https://blog-api-9n0c.onrender.com/docs)

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL (Neon) |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Authentication | JWT (PyJWT) |
| Password Hashing | pwdlib (Argon2) |
| Deployment | Render |

---

## 🚀 Features

- 🔐 **JWT Authentication** — secure token-based login with expiry
- 👮 **Role-Based Access Control** — Admin vs normal User permissions
- 📝 **Post Workflow** — create posts as draft, publish when ready
- 📄 **Pagination & Filtering** — browse posts by page, category, or author
- 💬 **Comments** — comment on any post, delete only your own
- ❤️ **Likes** — like/unlike posts with duplicate prevention at both application and database level
- 🗑️ **Cascade Deletion** — deleting a post removes all its comments and likes automatically
- 🔗 **SQLAlchemy Relationships** — navigate between models directly (`post.author`, `post.comments`, `user.posts`)
- 🛡️ **Ownership Protection** — users can only edit or delete their own content

---

## 📁 Project Structure

```
Blog-API/
├── main.py
├── requirements.txt
├── alembic.ini
├── migrations/
└── src/
    ├── user/
    │   ├── model.py
    │   ├── dtos.py
    │   ├── controller.py
    │   └── router.py
    ├── posts/
    │   ├── model.py
    │   ├── dtos.py
    │   ├── controller.py
    │   └── router.py
    ├── comments/
    │   ├── model.py
    │   ├── dtos.py
    │   ├── controller.py
    │   └── router.py
    ├── likes/
    │   ├── model.py
    │   ├── dtos.py
    │   ├── controller.py
    │   └── router.py
    ├── admin/
    │   ├── controller.py
    │   └── router.py
    └── utils/
        ├── db.py
        ├── helper.py
        └── settings.py
```

---

## 🛠️ Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/navneet-nitin/Blog-API.git
cd Blog-API
```

**2. Create and activate virtual environment**
```bash
python -m venv env

# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file in root directory**
```env
DB_CONNECTION=your_postgresql_connection_string
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**5. Run database migrations**
```bash
alembic upgrade head
```

**6. Start the server**
```bash
uvicorn main:app --reload
```

**7. Open Swagger UI**
```
http://localhost:8000/docs
```

---

## 📡 API Endpoints

### 👤 User
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/user/register` | ❌ | Register a new user |
| GET | `/user/login` | ❌ | Login and receive JWT token |
| GET | `/user/profile` | ✅ | View your profile |
| PUT | `/user/update` | ✅ | Update your details |
| DELETE | `/user/delete` | ✅ | Delete your account |

### 📝 Posts
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/post/create` | ✅ | Create a new post (saved as draft) |
| PUT | `/post/publish/{post_id}` | ✅ | Publish a draft post |
| GET | `/post/all` | ✅ | Get all published posts (paginated) |
| GET | `/post/get_post/{post_id}` | ✅ | Get a single post by ID |
| GET | `/post/get_my_posts` | ✅ | Get all your posts including drafts |
| PUT | `/post/update/{post_id}` | ✅ | Update your post |
| DELETE | `/post/delete/{post_id}` | ✅ | Delete your post |

**Pagination & Filtering:**
```
GET /post/all?limit=10&offset=0
GET /post/all?category=tech
GET /post/all?username=navneet_nitin
GET /post/all?category=tech&username=navneet_nitin
```

### 💬 Comments
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/comment/create/{post_id}` | ✅ | Comment on a post |
| PUT | `/comment/edit/{comment_id}` | ✅ | Edit your comment |
| DELETE | `/comment/delete/{comment_id}` | ✅ | Delete your comment |
| GET | `/comment/all/{post_id}` | ✅ | Get all comments on a post |

### ❤️ Likes
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/like/create/{post_id}` | ✅ | Like a post (once only) |
| DELETE | `/like/unlike/{post_id}` | ✅ | Unlike a post |
| GET | `/like/total/{post_id}` | ✅ | Get total likes on a post |

### 🛡️ Admin Only
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| DELETE | `/admin/delete_post/{post_id}` | ✅ Admin | Delete any post |
| DELETE | `/admin/delete_comment/{comment_id}` | ✅ Admin | Delete any comment |
| GET | `/admin/all_users` | ✅ Admin | View all registered users |

---

## 🔐 Authentication

All protected routes require a Bearer token in the request header:

```
Authorization: Bearer <your_jwt_token>
```

Get your token by calling `/user/login` with your credentials.

---

## 🌍 Environment Variables

| Variable | Description |
|---|---|
| `DB_CONNECTION` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key for JWT signing |
| `ALGORITHM` | JWT algorithm (e.g. HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry duration in minutes |

> ⚠️ Never commit your `.env` file to GitHub. It is already added to `.gitignore`.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
