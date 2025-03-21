from django.urls import path
from App.views import adminView, talentView

urlpatterns = [
    #  admin onboarding urls
    path("admin-log-in",adminView.AdminLoginView.as_view()),
    path("forgot-password",adminView.ForgotPasswordView.as_view()),
    path("send-otp",adminView.resendOTPView.as_view()),
    path("verify-otp",adminView.VerifyOTPViewAdminSide.as_view()),
    path("change-password",adminView.ChangePasswordByTokenView.as_view()),
    path("admin-details",adminView.GetAdminDetailsByTokenView.as_view()),
    path("update-details",adminView.UpdateAdminDetailsByTokenView.as_view()),
    path("admin-log-out",adminView.LogOutView.as_view()),

    # 

    # FAQs urls
    path("questions",adminView.AddQuestionsAndAnswersView.as_view()),
    path("update-question/<int:id>",adminView.UpdateQuestionsAnswersView.as_view()),
    path("delete-question/<int:id>",adminView.DeleteQuestionAnswerView.as_view()),
    path("get-all-FAQ",adminView.GetAllQuestionsAnswers.as_view()),
    path("get-questions-by-id/<int:id>",adminView.GetQuestionById.as_view()),

    # terms and conditions urls
    path("terms-and-condition",adminView.AddTermsAndConditions.as_view()),
    path("update-terms-and-conditions/<int:id>",adminView.UpdateTermsAndConditions.as_view()),
    path("get-all-terms-and-conditions",adminView.GetTermsAndConditions.as_view()),
    path("add-privacy-policy",adminView.AddPrivacyPolicy.as_view()),
    path("get-policy",adminView.GetPrivacyPolicy.as_view()),
    path("add-contact-us",adminView.AddCustomerSupport.as_view()),
    path("get-contact-us",adminView.getCustomerSupport.as_view()),
    path("add-service-fees",adminView.AddServiceFeesView.as_view()),
    path("get-service-fees",adminView.getServiceFeesView.as_view()),


    # manage customer urls
    path("customer-csv",adminView.CustomerCSV.as_view()),
    path("all-customers",adminView.GetAllCustomerView.as_view()),
    path("add-customer",adminView.AddCustomerByAdminView.as_view()),
    path("customers-details-by-id/<int:id>",adminView.GetAllCustomerDetailsByidView.as_view()),
    path("edit-customer-by-id/<int:id>",adminView.updateCustomerDetailsByAdminView.as_view()),
    path("delete-customer-by-id/<int:id>",adminView.DeleteCustomerByAdminView.as_view()),
    path("customer-bookings/<int:id>", adminView.BookingsOfCustomerView.as_view()),

    #
    path("update-status-of-user/<int:id>",adminView.UpdateStatusOfCustomerView.as_view()),

    # manage categories Urls
    path("category-csv",adminView.CategoryCSVView.as_view()),
    path("category", adminView.AddTalentCategoryView.as_view()),
    path("all-category", adminView.GetAllCategoriesView.as_view()),#this is with pagination 
    path("get-all-category",adminView.AllCategoryView.as_view()), # this is with out pagination for add artist 
    path("get-categories-details-by-id/<int:id>", adminView.GetCategoriesDetailsByIdView.as_view()),
    path("update-categories-detail-by-id/<int:id>", adminView.UpdateCategoriesByIdView.as_view()),
    path("delete-category-by-id/<int:id>",adminView.DeleteCategoriesByIdView.as_view()),
    path("sub-category-based-on-category",adminView.GetAllSubCategoryBasedOnCategoryView.as_view()),
    path("sub-category/", adminView.AddTalentSubCategoryView.as_view()),
    path("update-subcategory-by-id/<int:id>",adminView.UpdateSubcategoryByIdView.as_view()),
    path("get-subcategory-by-id/<int:id>",adminView.GetSubCategoryByIdView.as_view()),
    path("update-status-of-category/<int:id>", adminView.UpdateStatusOfCategoryView.as_view()),
    path("update-status-of-subcategory/<int:id>",adminView.UpdateStatusOfSubCategoryView.as_view()),
    path("delete-subcategory-by-id/<int:id>",adminView.DeleteSubcategoryByidView.as_view()),
    path("sub-categories", talentView.SubCategoryListingAngularView.as_view()),

    #manage artist urls
    path("artist-csv",adminView.ArtistCSVView.as_view()),
    path("get-all-artist-details", adminView.GetAllArtistDetialsView.as_view()),
    path("get-artist-details-by-id/<int:id>", adminView.GetArtistDetailsByIdView.as_view()),
    path("update-artist-details-by-id/<int:id>", adminView.UpdateArtistDetailsByIdView.as_view()),
    path("delete-artist-details-by-id/<int:id>", adminView.DeleteArtistByIdView.as_view()),
    path("add-artist", adminView.AddArtistThroughAdminView.as_view()),
    path("verify-artist/<int:id>", adminView.VerifyArtistView.as_view()),
    path("artist-bookings/<int:id>", adminView.BookingsOfArtistView.as_view()),

    # manage sub admin
    path("add-sub-admin", adminView.AddSubAdminView.as_view()),
    path("update-sub-admin/<int:id>", adminView.UpdateSubAdminView.as_view()),
    path("get-sub-admin/<int:id>", adminView.SubAdminByIdView.as_view()),
    path("get-all-sub-admin", adminView.GetAllSubAdminView.as_view()),
    path("delete-sub-admin/<int:id>", adminView.DeleteSubAdminByIdView.as_view()),

    
    # booking module Urls
    path("booking-csv",adminView.BookingCSVView.as_view()),
    path("bookings", adminView.AllBookingsView.as_view()),
    path("booking/<int:id>", adminView.BookingdetaisByIdView.as_view()),


    # Dashboard module urls

    path("kpi",adminView.DashboardKPIView.as_view()),
    path("client_chart",adminView.CustomerChartView.as_view()),
    path("revenue_chart",adminView.RevenueChartView.as_view()),
    path("artist_chart",adminView.ArtistChartView.as_view()),
    path("booking_chart",adminView.BookingChartView.as_view()),

    #notification
    path("notification-csv",adminView.NotificationCSVView.as_view()),
    path("add-notifications", adminView.AddNotificationsView.as_view()),
    path("all-notifications", adminView.GetNotificationsView.as_view()),

    #revenue urls 
    path("get-all-revenue-details",adminView.GetAllRevenueDetails.as_view()),
    path("export-revenue-csv",adminView.ExportRevenueCSVView.as_view()),

    ##rating and review urls 
    path("all-rating",adminView.GetALLRatingDetials.as_view()),
    path("export-rating-csv",adminView.ExportRatingCSVView.as_view()),

    # colour preferences
    path("add-attribute-colour", adminView.AddattributeColourView.as_view()),
    path("update-attribute-colour/<int:id>", adminView.UpdateAttributeColourView.as_view()),
    path("delete-attribute-colour/<int:id>", adminView.DeleteAttributeColourView.as_view()),
    path("all-attribute-colours", adminView.AllAttributeColourView.as_view()),

    # path("add-eye-colour", adminView.AddEyeColourView.as_view()),
    # path("get-eye-colour/<int:id>", adminView.GetEyeColourView.as_view()),
    # path("update-eye-colour/<int:id>", adminView.UpdateEyeColourView.as_view()),
    # path("delete-eye-colour/<int:id>", adminView.DeleteEyeColourView.as_view()),
    # path("all-eye-colours", adminView.AllEyeColourView.as_view()),

]
