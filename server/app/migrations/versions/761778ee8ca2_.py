"""empty message

Revision ID: 761778ee8ca2
Revises: 9ce751fbce98
Create Date: 2020-05-02 23:29:50.356990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "761778ee8ca2"
down_revision = "9ce751fbce98"
branch_labels = None
depends_on = None

face_url_base = "https://dofus-lab.s3.us-east-2.amazonaws.com/class/face/{}_M.png"
male_sprite_url_base = (
    "https://dofus-lab.s3.us-east-2.amazonaws.com/class/sprite/{}_M.png"
)
female_sprite_url_base = (
    "https://dofus-lab.s3.us-east-2.amazonaws.com/class/sprite/{}_F.png"
)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("class", sa.Column("face_image_url", sa.String(), nullable=True))
    op.add_column(
        "class", sa.Column("male_sprite_image_url", sa.String(), nullable=True)
    )
    op.add_column(
        "class", sa.Column("female_sprite_image_url", sa.String(), nullable=True)
    )
    conn = op.get_bind()
    res = conn.execute(
        "SELECT c.uuid, ct.name FROM class c JOIN class_translation ct ON c.uuid = ct.class_id WHERE locale='en';"
    )
    classes = res.fetchall()
    for dofus_class in classes:
        conn.execute(
            "UPDATE class SET face_image_url='{}', male_sprite_image_url='{}', female_sprite_image_url='{}' WHERE uuid='{}'".format(
                face_url_base.format(dofus_class[1]),
                male_sprite_url_base.format(dofus_class[1]),
                female_sprite_url_base.format(dofus_class[1]),
                dofus_class[0],
            )
        )
    op.alter_column("class", "face_image_url", nullable=False)
    op.alter_column("class", "male_sprite_image_url", nullable=False)
    op.alter_column("class", "female_sprite_image_url", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("class", "face_image_url")
    op.drop_column("class", "male_sprite_image_url")
    op.drop_column("class", "female_sprite_image_url")
    # ### end Alembic commands ###
