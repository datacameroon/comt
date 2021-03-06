# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Comment.category'
        db.add_column('cm_comment', 'category', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Comment.category'
        db.delete_column('cm_comment', 'category')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
        'cm.activity': {
            'Meta': {'object_name': 'Activity'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['cm.Comment']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'originator_user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'originator_activity'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['cm.Text']", 'null': 'True', 'blank': 'True'}),
            'text_version': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['cm.TextVersion']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cm.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'adminkey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'data': ('django.db.models.fields.files.FileField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'text_version': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['cm.TextVersion']", 'null': 'True', 'blank': 'True'})
        },
        'cm.comment': {
            'Meta': {'object_name': 'Comment'},
            'adminkey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'category': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_html': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'end_offset': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_wrapper': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_key': ('django.db.models.fields.CharField', [], {'default': "'gDcMRuTvHtD'", 'max_length': '20', 'db_index': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reply_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cm.Comment']", 'null': 'True', 'blank': 'True'}),
            'start_offset': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_wrapper': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'text_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cm.TextVersion']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cm.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {}),
            'raw_value': ('django.db.models.fields.TextField', [], {})
        },
        'cm.email': {
            'Meta': {'object_name': 'Email'},
            'bcc': ('django.db.models.fields.TextField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.TextField', [], {}),
            'to': ('django.db.models.fields.TextField', [], {})
        },
        'cm.notification': {
            'Meta': {'object_name': 'Notification'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adminkey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cm.Text']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cm.role': {
            'Meta': {'object_name': 'Role'},
            'anon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'global_scope': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'roles'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'cm.text': {
            'Meta': {'object_name': 'Text'},
            'adminkey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'last_text_version': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related_text'", 'null': 'True', 'to': "orm['cm.TextVersion']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'private_feed_key': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': 'None', 'max_length': '20', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cm.textversion': {
            'Meta': {'object_name': 'TextVersion'},
            'adminkey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'category_1': ('django.db.models.fields.CharField', [], {'default': "u'platinium'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'category_2': ('django.db.models.fields.CharField', [], {'default': "u'gold'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'category_3': ('django.db.models.fields.CharField', [], {'default': "u'silver'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'category_4': ('django.db.models.fields.CharField', [], {'default': "u'bronze'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'category_5': ('django.db.models.fields.CharField', [], {'default': "u'iron'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'mod_posteriori': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cm.Text']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cm.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'adminkey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'allow_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_email_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_suspended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_temp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'preferred_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'tags': ('tagging.fields.TagField', [], {'max_length': '1000'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'cm.userrole': {
            'Meta': {'unique_together': "(('role', 'user', 'text'),)", 'object_name': 'UserRole'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cm.Role']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cm.Text']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cm']
