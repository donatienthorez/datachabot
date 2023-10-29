
class Formatter:
    def format_sources(sources):
        formatted_sources = []
        for index, source in enumerate(sources, start=1):
            page_content = source.page_content
            metadata_source = source.metadata['source']
            formatted_source = f"Source {index}. {page_content} from **{metadata_source}** \n"
            formatted_sources.append(formatted_source)
        return '\n'.join(formatted_sources)

    