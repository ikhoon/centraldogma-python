# Copyright 2021 LINE Corporation
#
# LINE Corporation licenses this file to you under the Apache License,
# version 2.0 (the "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at:
#
#   https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import LetterCase, config, dataclass_json
from marshmallow import fields

from centraldogma.data.constants import DATE_FORMAT_ISO8601_MS


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PushResult:
    revision: int
    pushed_at: datetime = field(
        metadata=config(
            decoder=lambda x: datetime.strptime(x, DATE_FORMAT_ISO8601_MS),
            mm_field=fields.DateTime(format=DATE_FORMAT_ISO8601_MS),
        ),
    )
