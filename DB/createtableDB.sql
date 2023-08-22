USE [FlashCardDB]
GO

/****** Object:  Table [dbo].[PointDB]    Script Date: Aug. 04 2023 10:50:26 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[PointDB](
	[Latitude] [decimal](5, 2) NULL,
	[Longitude] [decimal](5, 2) NULL,
	[Description] [varchar](255) NULL
) ON [PRIMARY]
GO

