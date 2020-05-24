from db import db


class m_agama(db.Model):
    __tablename__ = 'md_agama'

    kd_agama = db.Column(db.VARCHAR(10), primary_key=True)
    nm_agama = db.Column(db.VARCHAR(100))
    keterangan = db.Column(db.VARCHAR(100))
    catatan = db.Column(db.TEXT)
    is_aktif = db.Column(db.VARCHAR(2), db.CheckConstraint(r"md_agama.is_aktif IN ('0', '1')"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __init__(self, kd_agama, nm_agama, keterangan, catatan, is_aktif, user_id):
        self.kd_agama = kd_agama
        self.nm_agama = nm_agama
        self.keterangan = keterangan
        self.catatan = catatan
        self.is_aktif = is_aktif
        self.user_id = user_id

    def json(self):
        return {'kd_agama': self.kd_agama, 'nm_agama': self.nm_agama, 'keterangan': self.keterangan, 
                'catatan': self.catatan, 'is_aktif': self.is_aktif, 'user_id': self.user_id}

    @classmethod
    def cari(cls, kd_agama):
        return cls.query.filter_by(kd_agama=kd_agama).first()

    def simpan(self):
        db.session.add(self)
        db.session.commit()

    def hapus(self):
        db.session.delete(self)
        db.session.commit()
