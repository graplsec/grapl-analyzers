from typing import Any

from grapl_analyzerlib.analyzer import Analyzer, OneOrMany
from grapl_analyzerlib.prelude import ProcessQuery, FileQuery, ProcessView
from grapl_analyzerlib.execution import ExecutionHit


class ProcessDeletesBinaryFile(Analyzer):

    def get_queries(self) -> OneOrMany[ProcessQuery]:
        return (
            ProcessQuery()
            .with_deleted_files(
                FileQuery()
                .with_spawned_from(
                    ProcessQuery()
                )
            )
        )

    def on_response(self, response: ProcessView, output: Any):
        output.send(
            ExecutionHit(
                analyzer_name="Process Deletes Binary File",
                node_view=response,
                risk_score=20,
            )
        )