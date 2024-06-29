from common.factories import UserFactory, ProfileFactory
from profiles.models import Profile
from profiles.views import ProfileDeactivateApi
import pytest


class TestProfileDeactivateApi:

    @pytest.mark.django_db
    def test_when_profile_not_found(self, auth_request) -> None:
        user = UserFactory()
        request = auth_request(
            user=user,
            method="POST",
            url="/profiles/999/deactivate",
        )

        response = ProfileDeactivateApi.as_view()(request, profile_id=999)

        assert 404 == response.status_code

    @pytest.mark.django_db
    def test_when_profile_deactivated(self, auth_request) -> None:
        user = UserFactory()
        profile = ProfileFactory(user=user, is_active=False)
        request = auth_request(
            user=user,
            method="POST",
            url=f"/profiles/{profile.id}/deactivate",
        )

        response = ProfileDeactivateApi.as_view()(request, profile_id=profile.id)

        assert 204 == response.status_code
        assert Profile.objects.filter(id=profile.id, is_active=False).exists()
