from pathlib import Path
import re
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = PROJECT_ROOT / "index.html"


class SiteStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX_HTML.read_text(encoding="utf-8")

    def test_index_file_exists(self):
        self.assertTrue(INDEX_HTML.exists())

    def test_page_title_present(self):
        self.assertIn("<title>Student Career AI Tools</title>", self.html)

    def test_only_three_project_sections_exist(self):
        project_ids = re.findall(r'<article class="project(?: [^"]+)?" id="([^"]+)"', self.html)
        self.assertEqual(
            project_ids,
            ["resume-feedback", "job-translator", "cover-letter-feedback"],
        )

    def test_featured_strip_has_three_cards(self):
        featured_items = re.findall(r'class="featured-item"', self.html)
        self.assertEqual(len(featured_items), 3)

    def test_resume_tool_has_single_user_input(self):
        self.assertIn('id="resume-bullets"', self.html)
        self.assertNotIn('id="resume-role"', self.html)

    def test_job_tool_has_single_user_input(self):
        self.assertIn('id="job-description"', self.html)
        self.assertNotIn('id="job-profile"', self.html)

    def test_cover_letter_tool_has_single_user_input(self):
        self.assertIn('id="cover-draft"', self.html)
        self.assertNotIn('id="cover-job"', self.html)
        self.assertNotIn('id="cover-resume"', self.html)

    def test_demo_inputs_have_feedback_status_messages(self):
        feedback_ids = ["resume-feedback", "job-feedback", "cover-feedback"]
        for feedback_id in feedback_ids:
            with self.subTest(feedback_id=feedback_id):
                self.assertIn(f'id="{feedback_id}"', self.html)
                self.assertIn('role="status"', self.html)
                self.assertIn('aria-live="polite"', self.html)

    def test_keyboard_submission_guidance_is_present(self):
        guidance = [
            "press command/ctrl + enter to get feedback",
            "press enter to see a clearer breakdown",
            "press command/ctrl + enter to get revision feedback",
        ]
        lowered_html = self.html.lower()
        for item in guidance:
            with self.subTest(item=item):
                self.assertIn(item, lowered_html)

    def test_navigation_links_match_three_projects(self):
        self.assertIn('href="#resume-feedback"', self.html)
        self.assertIn('href="#job-translator"', self.html)
        self.assertIn('href="#cover-letter-feedback"', self.html)

    def test_readme_submission_keywords_are_supported_by_site(self):
        required_text = [
            "AI Resume Feedback Tool",
            "AI Job Description Translator",
            "AI Cover Letter Feedback",
            "Interactive Demo",
        ]
        for item in required_text:
            with self.subTest(item=item):
                self.assertIn(item, self.html)


if __name__ == "__main__":
    unittest.main()
