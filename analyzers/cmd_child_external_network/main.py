
from typing import Any

from grapl_analyzerlib.analyzer import Analyzer, OneOrMany
from grapl_analyzerlib.prelude import ProcessQuery, ExternalIpQuery, ProcessView
from grapl_analyzerlib.execution import ExecutionHit


class BrowserCreatedFileExecuted(Analyzer):

    def get_queries(self) -> OneOrMany[ProcessQuery]:
        return (
            ProcessQuery()
            .with_process_name()
            .with_parent(ProcessQuery().with_process_name(eq="cmd.exe"))
            .with_created_connection(ExternalIpQuery())
        )

    def on_response(self, response: ProcessView, output: Any):
        output.send(
            ExecutionHit(
                analyzer_name="Cmd Child External Network",
                node_view=response,
                risk_score=5,
            )
        )


