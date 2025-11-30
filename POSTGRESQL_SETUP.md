# PostgreSQL Setup Guide for Django

## ⚠️ Important: Read This First

Your Django app is currently using **SQLite** which works perfectly for development.
This guide will help you switch to PostgreSQL when you're ready.

## Why This Guide Exists

You've been getting this error:
```
FATAL: password authentication failed for user "adminuser"
```

This happens because the PostgreSQL user `adminuser` doesn't exist yet or has a different password.

## Prerequisites

- ✅ PostgreSQL 18 is installed and running
- ✅ You need your `postgres` superuser password (set during PostgreSQL installation)

## Option 1: Using pgAdmin (Easiest - GUI Method)

pgAdmin is a visual tool installed with PostgreSQL. It's usually already authenticated.

### Steps:

1. **Open pgAdmin** (search for it in Windows Start menu)

2. **Expand the server tree** on the left:
   - Servers → PostgreSQL 18 → Right-click on "Login/Group Roles"

3. **Create the user:**
   - Right-click "Login/Group Roles" → Create → Login/Group Role
   - **General tab**: Name = `adminuser`
   - **Definition tab**: Password = `superuser123`
   - **Privileges tab**: Check ✅ "Can login?" and ✅ "Create databases?"
   - Click **Save**

4. **Create the database:**
   - Right-click "Databases" → Create → Database
   - **General tab**: Database = `appdb`, Owner = `adminuser`
   - Click **Save**

5. **Done!** Now uncomment PostgreSQL in `settings.py` and run:
   ```powershell
   python manage.py migrate
   ```

## Option 2: Using Command Line (For Advanced Users)

### Step 1: Find your postgres password

If you don't remember it, you can reset it:
1. Find `pg_hba.conf` in `C:\Program Files\PostgreSQL\18\data\`
2. Open as Administrator
3. Find the line with `127.0.0.1/32` and change `scram-sha-256` to `trust`
4. Save and restart PostgreSQL service:
   ```powershell
   Restart-Service postgresql-x64-18
   ```
5. Connect without password and reset it:
   ```powershell
   cd "C:\Program Files\PostgreSQL\18\bin"
   .\psql.exe -U postgres
   ALTER USER postgres WITH PASSWORD 'your_new_password';
   \q
   ```
6. Change `pg_hba.conf` back to `scram-sha-256`
7. Restart PostgreSQL service again

### Step 2: Run the setup SQL file

```powershell
cd "C:\Program Files\PostgreSQL\18\bin"
.\psql.exe -U postgres -f "c:\Users\srini\workspace\Novamber\Apps\mysite\setup_db_simple.sql"
```

Enter your postgres password when prompted.

### Step 3: Verify the setup

Test the connection:
```powershell
.\psql.exe -U adminuser -d appdb
```
Password: `superuser123`

If you see the `appdb=>` prompt, it worked! Type `\q` to exit.

### Step 4: Update Django settings

In `mysite/settings.py`, uncomment the PostgreSQL section and comment out SQLite:

```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "CONN_MAX_AGE": 60,
        "OPTIONS": {},
    }
}
```

### Step 5: Run migrations

```powershell
python manage.py migrate
```

## Option 3: Stay with SQLite (Recommended for Development)

SQLite is perfect for development:
- ✅ No setup required
- ✅ No separate database server
- ✅ File-based (easy to reset)
- ✅ Works identically to PostgreSQL for most Django features
- ✅ Can switch to PostgreSQL anytime for production

**You don't need PostgreSQL unless:**
- You're deploying to production
- You need PostgreSQL-specific features
- You're working with a team using PostgreSQL

## Troubleshooting

### "password authentication failed"
- The user doesn't exist → Use pgAdmin or run the SQL file
- Wrong password → Check `.env` file has `DB_PASSWORD=superuser123`

### "database appdb does not exist"
- Create it using pgAdmin or the SQL file

### "psql: command not found"
- Add to PATH or use full path: `C:\Program Files\PostgreSQL\18\bin\psql.exe`

## Quick Reference

**Your PostgreSQL credentials (from `.env`):**
- Database: `appdb`
- User: `adminuser`
- Password: `superuser123`
- Host: `127.0.0.1`
- Port: `5432`

**SQL file location:**
`c:\Users\srini\workspace\Novamber\Apps\mysite\setup_db_simple.sql`

## Need Help?

If you're stuck, just use SQLite for now. You can always switch to PostgreSQL later!
