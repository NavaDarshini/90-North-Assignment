from difflib import restore
from rest_framework.response import Response
from rest_framework.views import APIView
from App.services.clientService import ClientService
from rest_framework.permissions import AllowAny,IsAuthenticated

userservice = ClientService()

class SignUpView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        result = userservice.user_signup(request)
        return Response(result, result["status"])

class VerifyOtpViaMailView(APIView):
    permission_classes = (AllowAny,)
    def post(self , request):
        result = userservice.verify_otp(request)
        return Response(result , result["status"])

class LogInView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        result= userservice.login(request)
        return Response(result, result["status"])

class ResendOtpView(APIView):
    permission_classes = (AllowAny,)
    def post(self , request):
        result = userservice.resend_otp(request)
        return Response(result , result["status"])
    

################################ADDRESS MANAGE ##############################

class AddClientNewAddressDetailsView(APIView):
    def post(self, request):
        result = userservice.add_address_using_token(request)
        return Response(result, result["status"])

class EditClientAddressDetailsView(APIView):
    def put(self, request,id ):
        result = userservice.edit_address_details(request,id)
        return Response(result, result["status"])


class DeleteClientAddressDetailsBYIDView(APIView):
    def delete(self, request, id):
        result = userservice.delete_address_details_by_id(request, id)
        return Response(result, result["status"])

class ShowAllAddressesDetailsView(APIView):
    def get(self, request):
        result = userservice.show_all_address_with_token(request)
        return Response(result, result["status"])

class GetAddressDetialsByIdView(APIView):
    def get(self, request, id):
        result = userservice.get_addres_details_by_id(request, id)
        return Response(result, result["status"])


#-------------------------------booking talent -------------------------

class ListingAllCategories(APIView):
    def post(self, request):
        result = userservice.All_categories(request)
        return Response(result, status=result["status"])

class ListingAllCategoriesBasedOnCategoryView(APIView):
    def post(self, request):
        result = userservice.All_categories_based_on_search(request)
        return Response(result, status=result["status"])

class ListingAllSubCategoriesBasedOnCategories(APIView):
    def post(self, request):
        result = userservice.all_sub_categories(request)
        return Response(result, status=result["status"])

class ListingAllTalent(APIView):
    def post(self, request):
        result = userservice.talents_details(request)
        return Response(result, status=result["status"])

class TalentDetailsForBookingView(APIView):
    def get(self, request, talent_id):
        result = userservice.talents_details_for_booking(request, talent_id)
        return Response(result, status=result["status"])


class clientDetailsbyTokenView(APIView):
    def get(self, request):
        result = userservice.client_details_by_token(request)
        return Response(result, status=result["status"])

class ResetPassword(APIView):
    def post(self, request):
        result = userservice.User_reset_password(request)
        return Response(result,status=result["status"])

class TalentDetailsById(APIView):
    def get(self, request,id):
        result = userservice.view_talent_all_details_by_id(request,id)
        return Response(result, status=result["status"])

class BookTalentView(APIView):
    def post(self,request):
        result = userservice.book_talent(request)
        return Response(result,status=result["status"])

class GetTalentSlotsView(APIView):
    def post(self,request):
        result = userservice.get_slots_by_date(request)
        return Response(result,status=result["status"])

class GetAllBookTalentDetails(APIView):
    def get(self, request, id):
        result = userservice.get_booking_details_by_id(request, id)
        return Response(result,status=result["status"])

class FilterAndSortView(APIView):
    def post(self, request):
        result = userservice.filter_talent(request)
        return Response(result,status=result["status"])

class EditClientDetailsByTokenView(APIView):
    def put(self, request):
        result = userservice.edit_client_details_by_token(request)
        return Response(result,status=result["status"])

class FetchAllTalentServicesView(APIView):
    def get(self, request, id):
        result = userservice.talent_services(request, id)
        return Response(result,status=result["status"])

class OngoingBookingsView(APIView):
    def get(self, request):
        result = userservice.ongoing_bookings(request)
        return Response(result,status=result["status"])

class CompletedBookingsView(APIView):
    def get(self, request):
        result = userservice.completed_bookings(request)
        return Response(result,status=result["status"])

class CancelledBookingsView(APIView):
    def get(self, request):
        result = userservice.cancelled_bookings(request)
        return Response(result,status=result["status"])

class AcceptOrCancelBookingsView(APIView):
    def post(self, request, booking_id):
        result = userservice.accept_or_reject_counter_offer(request, booking_id)
        return Response(result,status=result["status"])

class MarkBookingCompletedView(APIView):
    def post(self, request, booking_id):
        result = userservice.mark_booking_completed(request, booking_id)
        return Response(result,status=result["status"])

class TagsListingView(APIView):
    def get(self, request):
        result = userservice.tags_listing(request)
        return Response(result,status=result["status"])

class CompletePaymentView(APIView):
    def get(self, request, booking_id):
        result = userservice.complete_payment(request, booking_id)
        return Response(result,status=result["status"])
