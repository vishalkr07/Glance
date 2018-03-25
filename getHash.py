import hashlib

def hashhex(s):
  """Returns a heximal formated SHA1 hash of the input string."""
  h = hashlib.sha1()
  h.update(s)
  return h.hexdigest()


def get_url_hashes(url_list):
  return [hashhex(url) for url in url_list]

url = ["http://web.archive.org/web/20150301041716id_/http://us.cnn.com/2015/02/25/us/massachusetts-man-selling-snow-feat/index.html"]
print get_url_hashes(url)