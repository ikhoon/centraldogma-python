#  Copyright 2021 LINE Corporation
#
#  LINE Corporation licenses this file to you under the Apache License,
#  version 2.0 (the "License"); you may not use this file except in compliance
#  with the License. You may obtain a copy of the License at:
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


def to_string(obj, **fields) -> str:
    items = vars(obj).items()
    if not fields:
        values = [f"{k}={v}" for k, v in items]
    else:
        values = [f"{k}={v}" for k, v in items if k in fields]

    return f"{obj.__class__.__name__}({','.join(values)})"