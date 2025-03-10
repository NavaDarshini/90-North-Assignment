from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from App.services.talentService import TalentService

talent_service = TalentService()

class TalentSignUpView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        result = talent_service.user_signup(request)
        return Response(result, status=result["status"])

class TalentLoginView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        result = talent_service.login(request)
        return Response(result, status=result["status"])
    
class SendEmailOrPhoneView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        result = talent_service.resend_otp(request)
        return Response(result, status=result["status"])

class VerifyMailOrPhoneView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        result = talent_service.verify_otp(request)
        return Response(result, status=result["status"])

class SubCategoryListingView(APIView):
    def post(self, request):
        result = talent_service.sub_category_listing(request)
        return Response(result, status=result["status"])

class SubCategoryListingAngularView(APIView):
    def post(self, request):
        result = talent_service.sub_category_listing_angular(request)
        return Response(result, status=result["status"])

class ProfileSetUpAndUpdateView(APIView):
    def put(self, request):
        result = talent_service.profile_setup_and_edit(request)
        return Response(result, status=result["status"])

class EditProfileByTokenView(APIView):
    def put(self, request):
        result = talent_service.edit_artist_details_by_token(request)
        return Response(result, status=result["status"])

class ResendOtpView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        result = talent_service.resend_otp(request)
        return Response(result, status=result["status"])

class ResendOtpAfterLoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        result = talent_service.resend_otp_after_login(request)
        return Response(result, status=result["status"])

class TalentUserDetailsView(APIView):
    def get(self, request):
        result = talent_service.user_details_by_token(request)
        return Response(result, status=result["status"])

#clientBookinglisting

class ClientUpcomingBookingListing(APIView):
    def get(self, request):
        result = talent_service.upcoming_clients_booking_listing(request)
        return Response(result, status=result["status"])

class RecentOffersView(APIView):
    def get(self, request):
        result = talent_service.recent_offers_of_talent(request)
        return Response(result, status=result["status"])

class AcceptedOffersView(APIView):
    def get(self, request):
        result = talent_service.accepted_offers_of_talent(request)
        return Response(result, status=result["status"])

class CounterOfferByTalentView(APIView):
    def post(self, request):
        result = talent_service.counter_offer(request)
        return Response(result, status=result["status"])

class AcceptOfferByTalentView(APIView):
    def post(self, request):
        result = talent_service.accept_offer(request)
        return Response(result, status=result["status"])

class DeclineOfferByTalentView(APIView):
    def post(self, request):
        result = talent_service.decline_offer(request)
        return Response(result, status=result["status"])

class ClientPastBookingListing(APIView):
    def get(self, request):
        result = talent_service.past_client_booking_listing(request)
        return Response(result, status=result["status"])

class CancelledBookingsView(APIView):
    def get(self, request):
        result= talent_service.cancelled_bookings(request)
        return Response(result, status=result["status"])

class AllCategoriesView(APIView):
    def get(self, request):
        result= talent_service.all_categories(request)
        return Response(result, status=result["status"])


############# slots ###############
class GenerateSlotsView(APIView):
    def post(self, request):
        result = talent_service.add_slots(request)
        return Response(result, status=result["status"])

class FetchWeeklyTimingsView(APIView):
    def get(self, request):
        result = talent_service.fetch_weekly_timings(request)
        return Response(result, status=result["status"])

class GetSlotsByDateView(APIView):
    def post(self, request):
        result = talent_service.get_slots_by_date(request)
        return Response(result, status=result["status"])

class NotificationsView(APIView):
    def get(self, request):
        result = talent_service.notifications(request)
        return Response(result, status=result["status"])
