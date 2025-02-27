# Copyright 2023 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""upgrade to latest

Revision ID: cfe2a22173fc
Revises: d1e8cfd8e575
Create Date: 2024-05-27 15:41:35.069014

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "cfe2a22173fc"
down_revision = "d1e8cfd8e575"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "idx_artifacts_v2_labels_name_value",
        "artifacts_v2_labels",
        ["name", "value"],
        unique=False,
    )
    op.drop_index("_feature_sets_tags_obj_name_fk", table_name="feature_sets_tags")
    op.drop_index(
        "_feature_vectors_tags_obj_name_fk", table_name="feature_vectors_tags"
    )
    op.drop_index("_functions_tags_obj_name_fk", table_name="functions_tags")
    op.drop_index("_marketplace_sources_uc", table_name="hub_sources")
    op.create_unique_constraint("_hub_sources_uc", "hub_sources", ["name"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("_hub_sources_uc", "hub_sources", type_="unique")
    op.create_index("_marketplace_sources_uc", "hub_sources", ["name"], unique=False)
    op.create_index(
        "_functions_tags_obj_name_fk", "functions_tags", ["obj_name"], unique=False
    )
    op.create_index(
        "_feature_vectors_tags_obj_name_fk",
        "feature_vectors_tags",
        ["obj_name"],
        unique=False,
    )
    op.create_index(
        "_feature_sets_tags_obj_name_fk",
        "feature_sets_tags",
        ["obj_name"],
        unique=False,
    )
    op.drop_index(
        "idx_artifacts_v2_labels_name_value", table_name="artifacts_v2_labels"
    )
    # ### end Alembic commands ###
