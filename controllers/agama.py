from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.agama import m_agama


class Agama(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('kd_agama', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('nm_agama', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('keterangan')
    parser.add_argument('catatan')
    parser.add_argument('is_aktif', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('user_id', required=True)
    parser.add_argument('order', required=True)

    @jwt_required()
    def post(self):
        data = Agama.parser.parse_args()
        data_item = {'kd_agama': data['kd_agama'], 'nm_agama': data['nm_agama'],'keterangan': data['keterangan'],
                     'catatan': data['catatan'], 'is_aktif': data['is_aktif'], 'user_id': data['user_id'],}
                     
        agama = m_agama.cari(data['kd_agama'])

        if data['order'] == 'add':

            if agama:
                agama.nm_agama = data['nm_agama']
                agama.keterangan = data['keterangan']
                agama.catatan = data['catatan']
                agama.is_aktif = data['is_aktif']
                agama.user_id = data['user_id']
                return {'message': 'Data berhasil diubah.'}
            else:
                agama = m_agama(**data_item)
                agama.simpan()
                return {'message': 'Data berhasil disimpan.'}

        elif data['order'] == 'del':

            if agama:
                agama.hapus()
                return {'message': 'Data berhasil dihapus.'}
            return {'message': 'Data tidak ditemukan.'}, 404
        
        else:
            if agama:
                return agama.json()
            else:
                return {'items': list(map(lambda x: x.json(), m_agama.query.all()))}
