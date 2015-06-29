# coding=utf-8
__author__ = 'cysnake4713'

# coding=utf-8
from openerp import tools
from openerp import models, fields, api
from openerp.tools.translate import _


class VoteConfig(models.Model):
    _name = 'odoosoft.vote.config'
    _description = 'Odoosoft Vote Config'

    name = fields.Char(u'名称')
    description = fields.Text(u'描述')

    is_register = fields.Boolean(u'可以报名')
    reg_start_date = fields.Date(u'报名开始日期')
    reg_end_date = fields.Date(u'报名截止日期')

    is_vote = fields.Boolean(u'可以评分')

    vote_start_date = fields.Date(u'评分开始时间')
    vote_end_date = fields.Date(u'评分截止日期')

    vote_users = fields.Many2many('res.users', 'odoosoft_vote_config_user_rel', 'config_id', 'user_id', u'评分人员')
    vote_types = fields.Many2many('odoosoft.vote.type', 'odoosoft_vote_config_type_rel', 'config_id', 'type_id', u'评分类型')


class RegisterRecord(models.Model):
    _name = 'odoosoft.vote.register.record'
    _rec_name = 'name'
    _description = 'Odoosoft Vote Register Record'

    name = fields.Char(u'作品名称')
    files = fields.Many2many('ir.attachment', 'odoosoft_vote_register_record_user_rel', 'record_id', 'attachment_id', u'作品上传')

    school = fields.Char(u'学校')
    student = fields.Char(u'学生')
    description = fields.Text(u'作品简介')


class VoteRecord(models.Model):
    _name = 'odoosoft.vote.vote.record'
    _rec_name = 'user'
    _description = 'Odoosoft Vote Vote Record'

    user = fields.Many2one('res.users', u'用户')
    # files = fields.Many2many('ir.attachment', 'odoosoft_vote_vote_record_user_rel', 'record_id', 'attachment_id', u'作品上传')
    lines = fields.One2many('odoosoft.vote.vote.record.line', 'record', u'评分')


class VoteRecordLine(models.Model):
    _name = 'odoosoft.vote.vote.record.line'
    _rec_name = 'register'
    _description = 'Odoosoft Vote Vote Record Line'

    record = fields.Many2one('odoosoft.vote.vote.record', 'Record')
    register = fields.Many2one('odoosoft.vote.register.record', u'作品')

    score = fields.Float(u'得分')


class VoteType(models.Model):
    _name = 'odoosoft.vote.type'
    _rec_name = 'name'
    _description = 'Odoosoft Vote Type'

    name = fields.Char('Name')
