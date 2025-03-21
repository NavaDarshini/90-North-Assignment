from django.urls import path
from App.views import uploadMediaView, adminView, chatView, ratingsView, talentView

urlpatterns = [
    path("media", uploadMediaView.UploadMediaView.as_view()),
    path("show-questions", adminView.GetAllQuestionsAnswers.as_view()),
    path("terms-and-conditions-show", adminView.GetTermsAndConditions.as_view()),

    #### Chat ####
    path("all-chats", chatView.GetChatsView.as_view()),
    path("conversation/<int:session_id>", chatView.ConversationView.as_view()),

    #### ratings ####
    path("ratings", ratingsView.AddRatingView.as_view()),
    path("user-ratings/<int:talent_id>", ratingsView.GetUserRatingView.as_view()),
    path("ratings/<int:talent_id>", ratingsView.GetUserRatingByKeyView.as_view()),

    ###change_password###
    path("change-password",adminView.ChangePasswordByTokenView.as_view()),

    ### notification
    path("notifications", talentView.NotificationsView.as_view()),

]