# -*- coding: utf-8 -*-

from odoo import fields, models


class PortfolioProfile(models.Model):
    _name = "portfolio.profile"
    _description = "Portfolio Profile"
    _order = "sequence, id"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    website_published = fields.Boolean(default=True)

    hero_badge = fields.Char(default="Available for freelance and product work")
    hero_title = fields.Char(required=True)
    hero_intro = fields.Text()
    typed_items = fields.Char(
        string="Typed Highlights",
        help="Comma-separated rotating text for the hero section.",
    )
    focus_text = fields.Char()
    based_in_text = fields.Char()
    working_style_text = fields.Char()

    about_title = fields.Char(default="Full-stack developer with a systems view")
    about_text = fields.Text()
    skills_intro = fields.Text()
    resume_intro = fields.Text()
    portfolio_intro = fields.Text()
    contact_intro = fields.Text()
    community_text = fields.Text()

    website_url = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    availability_text = fields.Char(default="Open for freelance projects")

    clients_count = fields.Integer(default=35)
    projects_count = fields.Integer(default=120)
    years_count = fields.Integer(default=10)

    profile_image = fields.Binary(attachment=True)
    hero_background_image = fields.Binary(attachment=True)

    social_link_ids = fields.One2many(
        "portfolio.social.link", "profile_id", string="Social Links"
    )
    skill_category_ids = fields.One2many(
        "portfolio.skill.category", "profile_id", string="Skill Categories"
    )
    experience_ids = fields.One2many(
        "portfolio.experience", "profile_id", string="Experience"
    )
    education_ids = fields.One2many(
        "portfolio.education", "profile_id", string="Education"
    )
    language_ids = fields.One2many(
        "portfolio.language", "profile_id", string="Languages"
    )
    project_ids = fields.One2many(
        "portfolio.project", "profile_id", string="Projects"
    )
    contact_item_ids = fields.One2many(
        "portfolio.contact.item", "profile_id", string="Contact Items"
    )

    def get_profile_image_url(self):
        self.ensure_one()
        return "/web/image/portfolio.profile/%s/profile_image" % self.id

    def get_hero_background_url(self):
        self.ensure_one()
        return "/web/image/portfolio.profile/%s/hero_background_image" % self.id


class PortfolioSocialLink(models.Model):
    _name = "portfolio.social.link"
    _description = "Portfolio Social Link"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    name = fields.Char(required=True)
    url = fields.Char(required=True)
    icon_class = fields.Char(
        default="bi bi-link-45deg",
        help="Bootstrap Icons class, for example bi bi-linkedin",
    )


class PortfolioSkillCategory(models.Model):
    _name = "portfolio.skill.category"
    _description = "Portfolio Skill Category"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    name = fields.Char(required=True)
    skill_ids = fields.One2many("portfolio.skill", "category_id", string="Skills")


class PortfolioSkill(models.Model):
    _name = "portfolio.skill"
    _description = "Portfolio Skill"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    category_id = fields.Many2one(
        "portfolio.skill.category", required=True, ondelete="cascade"
    )
    name = fields.Char(required=True)


class PortfolioExperience(models.Model):
    _name = "portfolio.experience"
    _description = "Portfolio Experience"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    title = fields.Char(required=True)
    company = fields.Char(required=True)
    period = fields.Char(required=True)
    highlights = fields.Text(
        help="One bullet per line. Each line will be shown as a separate item."
    )


class PortfolioEducation(models.Model):
    _name = "portfolio.education"
    _description = "Portfolio Education"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    title = fields.Char(required=True)
    institution = fields.Char(required=True)
    year = fields.Char(required=True)


class PortfolioLanguage(models.Model):
    _name = "portfolio.language"
    _description = "Portfolio Language"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    name = fields.Char(required=True)
    level = fields.Char(required=True)


class PortfolioProject(models.Model):
    _name = "portfolio.project"
    _description = "Portfolio Project"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    name = fields.Char(required=True)
    project_type = fields.Char(required=True)
    summary = fields.Text(required=True)
    project_url = fields.Char()
    image = fields.Binary(attachment=True)

    def get_image_url(self):
        self.ensure_one()
        return "/web/image/portfolio.project/%s/image" % self.id


class PortfolioContactItem(models.Model):
    _name = "portfolio.contact.item"
    _description = "Portfolio Contact Item"
    _order = "sequence, id"

    sequence = fields.Integer(default=10)
    profile_id = fields.Many2one("portfolio.profile", required=True, ondelete="cascade")
    label = fields.Char(required=True)
    value = fields.Char(required=True)
    link = fields.Char()
    icon_class = fields.Char(
        default="bi bi-envelope",
        help="Bootstrap Icons class, for example bi bi-telephone",
    )
