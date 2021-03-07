from app import db


class Action(db.Model):

    __tablename__ = 'action'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254), nullable=False)
    description = db.Column(db.String(2047), nullable=False)
    unit = db.Column(db.String(254), nullable=False) # count or km or minute or hour
    impact = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(2047), nullable=True)
    family_id = db.Column(db.Integer, db.ForeignKey('action_family.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        id,
        name,
        description,
        unit,
        impact,
        source,
        family_id,
        score
    ):
        self.id = id
        self.name = name
        self.description = description
        self.unit = unit
        self.impact = impact
        self.source = source
        self.family_id = family_id
        self.score = score

    def __str__(self):
        if self.unit == "count":
            self.unit = ''

        return self.name + " with an impact of " + str(self.impact) + "gCO2eq."


    @staticmethod
    def get_list():
        actions = []
        try:
            query = db.session.query(Action)
            for c in query:
                actions.append(Action.to_array(c))
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return actions

    # Get by id
    @staticmethod
    def get_by_id(id):
        try:
            action = db.session.query(Action).get(id)
            if action is None:
                raise Exception(
                    'Get : Action with the ID ' + str(id) + ' not found'
                )
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return action

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
    def update(self, new_action):
        try:
            # merge and commit
            db.session.merge(new_action)
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            raise Exception(str(err))
        finally:
            db.session.close()

        return new_action

    # To Array
    def to_array(self):
        # Create JSON object
        action = {}
        action['id'] = self.id
        action['name'] = self.name
        action['description'] = self.description
        action['unit'] = self.unit
        action['impact'] = self.impact
        action['source'] = self.source
        action['family_id'] = self.family_id
        action['score'] = self.score

        return action
