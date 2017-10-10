# router
from handlers import indexHandler

router = []
router.extend(indexHandler.routers)
# todo
# router.append(r"/(.*)",ErrorHandler)