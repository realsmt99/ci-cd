def get_all_users(db):
  results = db.query("users").all()
  return results

def has_user_expired(user) -> bool:
  res = user.expiration_date < dt.datetime.now() 
  return res

def find_expired_users(db):
  expired_users = []
  users = get_all_users(db)
  for user in users:
      if has_user_expired(user):
          expired_users.append(user.id)
  return expired_users







