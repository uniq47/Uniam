# class Cart():
#     def __init__(self, request):
#         self.session = request.session
#         #obrain returing users existing session
#         cart = self.session.get('session_key')
        
#         # generate new session for new user
#         if 'session_key' not in request.session:
#             cart = self.session['session_key'] = {}
#         self.cart = cart
            
        