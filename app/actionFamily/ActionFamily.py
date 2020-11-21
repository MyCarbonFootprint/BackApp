from app import db


class ActionFamily(db.Model):

    __tablename__ = 'action_family'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254), nullable=False)
    description = db.Column(db.String(2047), nullable=False)


    def __init__(
        self,
        id,
        name,
        description
    ):
        self.id = id
        self.name = name
        self.description = description


    @staticmethod
    def get_list():
        action_families = []
        try:
            query = db.session.query(ActionFamily)
            for c in query:
                action_families.append(ActionFamily.to_array(c))
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return action_families

    # Get by id
    @staticmethod
    def get_by_id(id):
        try:
            action_family = db.session.query(ActionFamily).get(id)
            if action_family is None:
                raise Exception(
                    'Get : ActionFamily with the ID ' + str(id) + ' not found'
                )
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return action_family

    # Create
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return self

    # Update
    def update(self, new):
        try:
            # merge and commit
            db.session.merge(new)
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return new

    # To Array
    def to_array(self):
        # Create JSON object
        action_family = {}
        action_family['id'] = self.id
        action_family['name'] = self.name
        action_family['description'] = self.description

        return action_family
